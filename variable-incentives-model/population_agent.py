from mesa import Agent

class PopulationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.behavior = "neutral"  # Initial behavior: neutral
        self.energy = 100  # Resource or energy the agent has
        self.good_action_probability = 0.5  # Start with 50% chance of good actions

    def step(self):
        # Agent's action choice based on the adaptive good action probability
        if self.random.random() < self.good_action_probability:
            self.do_good_action()
        else:
            self.do_bad_action()

        # Apply environmental consequences of behavior
        self.update_behavior()

    def do_good_action(self):
        self.behavior = "good"
        self.energy -= 1  # Small energy cost for doing good actions
        self.model.environment_health += 2  # Positive impact on environmental health

    def do_bad_action(self):
        self.behavior = "bad"
        self.energy += 1  # Small energy gain for bad actions
        self.model.environment_health -= 20  # Significant negative impact on environment

    def update_behavior(self):
        # Calculate the proportion of good behavior in the model
        p_good = self.model.calculate_proportion_good()

        # Adjust rewards and penalties based on behavior proportion
        if self.behavior == "bad":
            penalty = -5 * (1 / (p_good + 0.01))  # Increased penalty when good behavior is low
            self.energy += penalty
            self.good_action_probability += 0.005  # Encourage good behavior

        elif self.behavior == "good":
            reward = 5 * (1 / (p_good + 0.01))  # Increased reward when good behavior is low
            self.energy += reward
            self.good_action_probability += 0.001  # Slight increase in good action probability

        # Cap the good action probability between 0.5 and 1.0 (50% to 100%)
        self.good_action_probability = max(0.5, min(self.good_action_probability, 1.0))
