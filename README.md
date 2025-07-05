# Quantum NQueens

## Solving NQueens using quantum computing 

After becoming obsessed with this problem as I implemented a solution [here](https://github.com/Dpbm/n-rainhas) and [here](https://github.com/Dpbm/faculdade/tree/master/quarto-ano/python/my-nqueens) for my AI class at college. I decided to put an end in this story and implement the final version using quantum computing.

At first, I implemented 2 versions one using `Qubo` and the other `QAOA`. Even thought the `QAOA` approach was kinda trick to get good results, I put a lot of effort on that. 

During the implementation of this code, I came across [this paper](https://arxiv.org/pdf/2312.16312), proposing an specific quantum circuit for solving NQueens. I really liked the idea so I decided to create another version based on `Grover's algorithm` by my own.

## Using the code

To ease the process of setting up this code, you can use it at:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Dpbm/qnqueens/HEAD)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Dpbm/qnqueens/)

But you can also run it on your local machine. To do that, first install [uv](https://github.com/astral-sh/uv) and then run:

```bash
uv sync
jupyter lab
```
