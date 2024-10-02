from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from variable_population_agent import PopulationAgent

class PopulationModel(Model):
    def __init__(self, width, height, N, duration):
        self.name = "Var Model"
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.environment_health = 100  # Environmental health starts at 100 (good)
        self.duration = duration

        # Create agents
        for i in range(self.num_agents):
            agent = PopulationAgent(i, self)
            # print(agent.get_name())
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Environment Health": "environment_health"},
            agent_reporters={"Behavior": "behavior"}
        )

    def get_name(self):
        return self.name
        
    def calculate_proportion_good(self):
        good_count = sum(1 for agent in self.schedule.agents if agent.behavior == "good")
        return good_count / self.num_agents if self.num_agents > 0 else 0

    def get_duration(self):
        """Return the duration of the model."""
        return self.duration

    def step(self):
        # Collect data at each step
        self.datacollector.collect(self)

        # Update agents' actions and the environment
        self.schedule.step()

        # Ensure environmental health remains within reasonable bounds (0 to 200)
        self.environment_health = max(0, min(self.environment_health, 200))
