# Week 3 — Advanced Python + Maths Intro for ML

## Topics Covered

| Day | Topic |
|-----|-------|
| Day 15 | Generators + Iterators |
| Day 16 | Decorators |
| Day 17 | Modules, Packages, Virtual Environments |
| Day 18 | Type Hints + Context Managers |
| Day 19 | Maths Intro — Set Notation, Sigma, First NumPy |
| Day 20 | Linear Algebra Intro — Vectors + Matrices |
| Day 21 | Week 3 Mini Project |

## Concepts Used

- Custom iterators (`__iter__`, `__next__`)
- Generator functions (`yield`)
- Decorators with `*args`/`**kwargs`
- Modules and packages (`__init__.py`)
- Virtual environments and `requirements.txt`
- Type hints (`List`, `Dict`, `Optional`)
- Context managers (`__enter__`, `__exit__`, `@contextmanager`)
- Set notation and math-to-Python translation
- Sigma notation as summation formulas
- NumPy arrays, vectors, dot product, norm
- Matrix operations and matrix multiplication shape rules

## Mini Project — ML Data Pipeline Toolkit

### Description
A small data pipeline that batches a dataset using a generator,
times each batch with a decorator, wraps the whole run in a
context manager, and calculates predictions using NumPy matrix
multiplication.

### Files
- `pipeline_tools/decorators.py` — timer decorator
- `pipeline_tools/batch_generator.py` — batch generator
- `numpy_ops.py` — vector and matrix operations
- `day21_p60_main.py` — main pipeline script

### How to Run
```bash
cd day21_project
python day21_p60_main.py
```

### Author
Harshit | BTech CSE 3rd Year | ML Journey Week 3