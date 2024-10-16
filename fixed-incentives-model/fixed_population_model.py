from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from fixed_population_agent import PopulationAgent

class PopulationModel(Model):
    def __init__(self, width, height, N, duration):
        self.num_agents = N
        self.name = "Fixed Model"
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.environment_health = 0  # Environmental health starts at 100 (good)
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
        
    def get_duration(self):
        return self.duration

    def step(self):
        # Collect data at each step
        self.datacollector.collect(self)

        # Update agents' actions and the environment
        self.schedule.step()

        # Gradual natural recovery of the environment, slowed down (e.g., +0.2 per step)
        # self.environment_health += 0.2

        # Ensure environmental health remains within reasonable bounds (0 to 200)
        # if self.environment_health > 200:
        #     self.environment_health = 200
        # elif self.environment_health < 0:
        #     self.environment_health = 0
