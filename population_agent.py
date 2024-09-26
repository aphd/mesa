from mesa import Agent

class PopulationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.behavior = "neutral"  # Initial behavior: neutral
        self.energy = 100  # Resource or energy the agent has

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
        self.energy -= 10  # Helping the environment takes effort/resources
        self.model.environment_health += 5  # Improves environmental health

    def do_bad_action(self):
        # Bad actions benefit the agent in the short term but harm the environment
        self.behavior = "bad"
        self.energy += 10  # Gaining energy/resources by exploiting the environment
        self.model.environment_health -= 5  # Degrades the environment

    def update_behavior(self):
        # Agents can receive penalties for bad behavior or rewards for good
        if self.behavior == "bad" and self.model.environment_health < 50:
            # Penalize agents when the environment is in poor health
            self.energy -= 5
        elif self.behavior == "good" and self.model.environment_health > 70:
            # Reward agents when the environment is healthy
            self.energy += 5
