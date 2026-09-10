# ============================================
# Day 27 - Program 78
# Topic: Chain Rule Simulation — Mini Neuron
# Concepts: forward pass, backward pass, chain rule,
#           verifying gradients numerically
# ============================================


def forward_pass(x: float, w: float, b: float) -> dict:
    # I compute the forward pass of a tiny neuron:
    # a linear step followed by a squaring step.
    z = w * x + b
    y = z ** 2
    return {"z": z, "y": y}


def backward_pass(x: float, z: float) -> float:
    # I compute dy/dw using the chain rule:
    # dy/dw = dy/dz * dz/dw
    dy_dz = 2 * z
    dz_dw = x
    return dy_dz * dz_dw


def backward_pass_bias(z: float) -> float:
    # I compute dy/db using the chain rule.
    # dz/db is always 1, so dy/db = dy/dz.
    dy_dz = 2 * z
    dz_db = 1
    return dy_dz * dz_db


def numerical_gradient_w(x: float, w: float, b: float, h: float = 1e-6) -> float:
    # I verify the chain rule result by nudging w slightly
    # and measuring how much the output changes.
    y_plus = forward_pass(x, w + h, b)["y"]
    y_minus = forward_pass(x, w - h, b)["y"]
    return (y_plus - y_minus) / (2 * h)


def one_training_step(x: float, y_target: float, w: float, b: float, lr: float) -> dict:
    # I run one full training step: forward pass, compute
    # gradients, then update the weight and bias.
    forward = forward_pass(x, w, b)
    grad_w = backward_pass(x, forward["z"])
    grad_b = backward_pass_bias(forward["z"])

    new_w = w - lr * grad_w
    new_b = b - lr * grad_b

    return {"w": new_w, "b": new_b, "output": forward["y"]}


# --- TESTING ---

x, w, b = 2.0, 3.0, 1.0

result = forward_pass(x, w, b)
print(f"Forward pass: z={result['z']}, y={result['y']}")

grad_w_manual = backward_pass(x, result["z"])
grad_w_numerical = numerical_gradient_w(x, w, b)
print(f"Manual gradient: {grad_w_manual}")
print(f"Numerical gradient: {grad_w_numerical:.4f}")

grad_b = backward_pass_bias(result["z"])
print(f"Bias gradient: {grad_b}")

# I run several training steps and watch the output shrink.
print("\nTraining steps:")
current_w, current_b = 3.0, 1.0
for step in range(5):
    step_result = one_training_step(x, 0, current_w, current_b, lr=0.01)
    print(f"Step {step+1}: w={step_result['w']:.4f}, "
          f"b={step_result['b']:.4f}, output={step_result['output']:.4f}")
    current_w, current_b = step_result["w"], step_result["b"]

