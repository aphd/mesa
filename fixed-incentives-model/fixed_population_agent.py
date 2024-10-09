from mesa import Agent

class PopulationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.name = "Fixed Agent"
        self.behavior = "neutral"  # Initial behavior: neutral
        self.energy = 100  # Resource or energy the agent has
        self.good_action_probability = 0.5  # Start with 50% chance of good actions
        self.token = 0  # Initialize token variable
    
    def get_name(self):
        return self.name
    
    def step(self):
        # Agent's action choice based on the adaptive good action probability
        if self.random.random() < self.good_action_probability:
            self.do_good_action()
        else:
            self.do_bad_action()

        # Apply environmental consequences of behavior
        self.update_behavior()

    def do_good_action(self):
        # Good actions improve the environment more slowly
        self.behavior = "good"
        self.energy -= 1  # Small energy cost for doing good actions
        self.model.environment_health += 2  # Decreased positive impact on environmental health
        self.token += 1  # Increase token for good action

    def do_bad_action(self):
        # Bad actions now have minimal impact on the environment
        self.behavior = "bad"
        self.energy += 1  # Small energy gain for bad actions
        self.model.environment_health -= 20  # Very limited negative impact on environment
        self.token -= 1  # Decrease token for bad action

    def update_behavior(self):
        # If penalized for bad behavior (when environment is poor)
        if self.behavior == "bad" and self.model.environment_health < 50:
            self.energy -= .01  # Smaller penalty for bad actions
            self.good_action_probability += 0.0051  # Small increase in good action probability

        # If rewarded for good behavior (when environment is healthy)
        elif self.behavior == "good" and self.model.environment_health > 70:
            self.energy += .01  # Smaller reward for good actions
            self.good_action_probability += 0.0001  # Small increase in good action probability

        # Cap the good action probability between 0.5 and 1.0 (50% to 100%)
        if self.good_action_probability > 1.0:
            self.good_action_probability = 1.0
        elif self.good_action_probability < 0.5:
            self.good_action_probability = 0.5