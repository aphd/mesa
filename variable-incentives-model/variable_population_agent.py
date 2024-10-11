from mesa import Agent

class PopulationAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.name = "Variable Agent"
        self.behavior = "neutral"  # Initial behavior: neutral
        self.energy = 100  # Resource or energy the agent has
        self.good_action_probability = 0.5  # Start with 50% chance of good actions
        self.token = 0  # Initialize token variable
        self.max_token = 12

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

        # Set token reward/penalty based on behavior proportion
        if self.behavior == "bad":
            token_penalty = self.max_token * (1 - p_good)  # Higher penalty when good behavior is low
            self.token -= token_penalty  # Decrease tokens based on penalty
            token_reward = 0  # No reward when behavior is bad
        elif self.behavior == "good":
            token_reward = self.max_token * (1 - p_good)  # Lower reward when good behavior is high
            self.token += max(token_reward, 0.2)  # Ensure token never goes below 0.2

        # Adjust good action probability based on the reward earned
        reward_factor = token_reward / self.max_token  # Normalized reward factor between 0 and 1
        self.good_action_probability += reward_factor * 0.05  # Increase probability proportionally to reward

        # Cap the good action probability between 0.5 and 1.0 (50% to 100%)
        self.good_action_probability = max(0.5, min(self.good_action_probability, 1.0))
