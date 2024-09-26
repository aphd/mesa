from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

class PopulationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.behavior = "neutral"  # Initial behavior: neutral
        self.food = 100  # Resource or energy the agent has

    def step(self):
        # Agent decides whether to perform a good or bad action
        if self.random.random() < 0.5:
            self.do_good_action()
        else:
            self.do_bad_action()

        # Apply environmental consequences of behavior
        self.update_behavior()

    def do_good_action(self):
        # Good actions improve the environment, but may cost the agent resources
        self.behavior = "good"
        self.food -= 10  # Helping the environment takes effort/resources
        self.model.environment_health += 5  # Improves environmental health

    def do_bad_action(self):
        # Bad actions benefit the agent in the short term but harm the environment
        self.behavior = "bad"
        self.food += 10  # Gaining food/resources by exploiting the environment
        self.model.environment_health -= 5  # Degrades the environment

    def update_behavior(self):
        # Agents can receive penalties for bad behavior or rewards for good
        if self.behavior == "bad" and self.model.environment_health < 50:
            # Penalize agents when the environment is in poor health
            self.food -= 5
        elif self.behavior == "good" and self.model.environment_health > 70:
            # Reward agents when the environment is healthy
            self.food += 5


class PopulationModel(Model):
    def __init__(self, width, height, N):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.environment_health = 100  # Environmental health starts at 100 (good)

        # Create agents
        for i in range(self.num_agents):
            agent = PopulationAgent(i, self)  # Now this is defined
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Environment Health": "environment_health"},
            agent_reporters={"Behavior": "behavior"}
        )

    def step(self):
        # Collect data at each step
        self.datacollector.collect(self)

        # Update agents' actions and the environment
        self.schedule.step()

        # Ensure environmental health remains within reasonable bounds
        if self.environment_health > 100:
            self.environment_health = 100
        elif self.environment_health < 0:
            self.environment_health = 0
