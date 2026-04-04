from functools import lru_cache
import time

# ─────────────────────────────────
# Part A: Three Fibonacci Versions
# ─────────────────────────────────

# Version 1: Recursive (slow)
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Version 2: LRU Cache (fast)
@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1: return n
    return fib_lru(n-1) + fib_lru(n-2)

# Version 3: Manual dict cache (manual)
_fib_cache = {}
def fib_manual_cache(n):
    if n in _fib_cache:
        return _fib_cache[n]    # cache hit!
    if n <= 1:
        return n
    result = (fib_manual_cache(n-1) +
              fib_manual_cache(n-2))
    _fib_cache[n] = result      # cache store
    return result

# Version 4: Iterative (fastest)
def fib_iterative(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

# Compare all versions:
print("="*50)
print("FIBONACCI COMPARISON")
print("="*50)

test_n = 35

for name, func in [
    ("Recursive",     fib_recursive),
    ("LRU Cache",     fib_lru),
    ("Manual Cache",  fib_manual_cache),
    ("Iterative",     fib_iterative),
]:
    start = time.time()
    result = func(test_n)
    elapsed = time.time() - start
    print(f"{name:<15}: fib({test_n})={result} "
          f"| {elapsed:.6f}s")

# ─────────────────────────────────
# Part B: ML Training Tracker
# Using Closures + Nonlocal
# ─────────────────────────────────

def create_training_tracker(patience=3):
    """
    Training loss tracker with early stopping.
    Uses closure to maintain state.

    patience = kitne epochs
               improvement nahi hoti toh stop
    """
    best_loss       = float('inf')  # enclosed
    epochs_no_improv = 0             # enclosed
    history         = []             # enclosed
    epoch_num       = 0              # enclosed

    def update(loss):
        nonlocal best_loss, epochs_no_improv
        nonlocal epoch_num
        epoch_num += 1
        history.append(loss)

        if loss < best_loss:
            best_loss = loss
            epochs_no_improv = 0
            improved = True
        else:
            epochs_no_improv += 1
            improved = False

        should_stop = (
            epochs_no_improv >= patience
        )

        return {
            "epoch":      epoch_num,
            "loss":       loss,
            "best_loss":  best_loss,
            "improved":   improved,
            "no_improve": epochs_no_improv,
            "stop":       should_stop
        }

    def get_history():
        return history.copy()

    def get_best():
        return best_loss

    def reset():
        nonlocal best_loss, epochs_no_improv
        nonlocal epoch_num
        best_loss        = float('inf')
        epochs_no_improv = 0
        epoch_num        = 0
        history.clear()

    def plot_ascii():
        """ASCII loss curve."""
        if not history:
            return
        min_l = min(history)
        max_l = max(history)
        height = 10
        width  = len(history)

        print("\nLoss Curve:")
        for row in range(height):
            threshold = max_l - (row/height) * \
                        (max_l - min_l)
            line = ""
            for loss in history:
                line += "█" if loss >= threshold \
                        else " "
            label = f"{threshold:.2f}" \
                    if row % 3 == 0 else "    "
            print(f"  {label}|{line}")
        print("      " + "-"*width)
        print(f"      Epochs 1 → {len(history)}")

    return update, get_history, get_best, \
           reset, plot_ascii

# Test the tracker:
print("\n" + "="*50)
print("ML TRAINING TRACKER")
print("="*50)

update, get_hist, get_best, \
reset, plot = create_training_tracker(patience=3)

# Simulate training losses:
simulated_losses = [
    0.95, 0.82, 0.74, 0.68,
    0.61, 0.59, 0.58, 0.59,   # plateau
    0.60, 0.61                  # getting worse
]

print("\nTraining Progress:")
print("-"*50)

for loss in simulated_losses:
    info = update(loss)
    status = "↓ BEST" if info["improved"] \
             else f"⚠ No improve " \
                  f"({info['no_improve']}/{3})"

    print(f"  Epoch {info['epoch']:2d} | "
          f"Loss: {info['loss']:.3f} | "
          f"Best: {info['best_loss']:.3f} | "
          f"{status}")

    if info["stop"]:
        print(f"\n  🛑 Early stopping triggered!")
        print(f"     Best loss: {info['best_loss']:.3f}")
        print(f"     At epoch: "
              f"{info['epoch'] - 3}")
        break

print(f"\nFull history: {get_hist()}")
plot()

