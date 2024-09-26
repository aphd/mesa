from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from population_agent import PopulationAgent

class PopulationModel(Model):
    def __init__(self, width, height, N):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.environment_health = 100  # Environmental health starts at 100 (good)

        # Create agents
        for i in range(self.num_agents):
            agent = PopulationAgent(i, self)
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
