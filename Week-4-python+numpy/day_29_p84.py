# ============================================
# Day 29 - Program 84
# Topic: Config-Driven Gradient Descent (Synthesis)
# Concepts: @property validation, gradient descent,
#           combining Week 2 and Week 4 concepts
# ============================================


class TrainingConfig:

    def __init__(self, learning_rate: float, epochs: int):
        self._learning_rate = None
        self._epochs = None
        self.learning_rate = learning_rate
        self.epochs = epochs

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if not (0 < value < 1):
            raise ValueError("learning_rate must be between 0 and 1")
        self._learning_rate = value

    @property
    def epochs(self):
        return self._epochs

    @epochs.setter
    def epochs(self, value):
        if value <= 0:
            raise ValueError("epochs must be positive")
        self._epochs = value


def gradient(x):
    return 2 * x - 4   # derivative of x^2 - 4x + 4


def train(config: TrainingConfig, start_x: float) -> dict:
    x = start_x
    history = []
    for _ in range(config.epochs):
        loss = x**2 - 4*x + 4
        history.append(loss)
        x = x - config.learning_rate * gradient(x)
    return {"final_x": x, "loss_history": history}


# --- TESTING ---
config = TrainingConfig(learning_rate=0.1, epochs=50)
result = train(config, start_x=10)
print(f"Final x: {result['final_x']:.4f}")
print(f"Final loss: {result['loss_history'][-1]:.4f}")

try:
    bad_config = TrainingConfig(learning_rate=1.5, epochs=50)
except ValueError as e:
    print(f"Caught: {e}")