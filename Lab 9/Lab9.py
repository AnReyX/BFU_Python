import numpy as np
from itertools import groupby
from scipy.stats import multivariate_normal
import time

def task_1():
    arr = np.array([])
    with open("input.txt") as f:
        for line in f:
            arr = np.concatenate((arr, [int(i) for i in line.split(',')]))
    print(f"Sum of arr: {arr.sum()}, Min: {arr.min()}, Max: {arr.max()}")


def task_2():
    x = np.array([2, 2, 2, 3, 3, 3, 5])
    values = []
    counts = []

    for val, group in groupby(x):
        values += [val]
        counts += [len(list(group))]

    ans = (np.array(values), np.array(counts))
    print(ans)


def task_3():
    arr = np.random.randn(10, 4)
    min_val = arr.min()
    max_val = arr.max()
    mean_val = arr.mean()
    std_val = arr.std()
    fir_fiv_rows = arr[:5]

    print(f"Random array (10x4): {arr},")
    print(f"Minimum: {min_val}, Maximum: {max_val}, Mean: {mean_val}, Std: {std_val}")
    print(f"First five rows: {fir_fiv_rows}")


def task_4():
    x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
    indexes = np.where(x[:-1] == 0)[0] + 1
    after_zero = x[indexes]

    print(f"Elements after zero: {after_zero}; their maximum: {after_zero.max()}")


#task 5
def logpdf_mvn(X, m, C):
    N, D = X.shape
    X_centered = X - m
    inv_C = np.linalg.inv(C)
    sign, logdet_C = np.linalg.slogdet(C)
    if sign != 1:
        raise ValueError("Covariate maatrix should be positive")
    quad_form = np.einsum('ni,ij,nj->n', X_centered, inv_C, X_centered)
    log_density = -0.5 * (D * np.log(2 * np.pi) + logdet_C + quad_form)
    return log_density

def task_5():
    X = np.array([
        [1.0, 2.0],
        [0.5, -0.2],
        [-1.0, 1.5]
    ])
    m = np.array([0.0, 0.0])
    C = np.array([[1.0, 0.2],
                  [0.2, 2.0]])

    my_logpdf = logpdf_mvn(X, m, C)

    rv = multivariate_normal(mean=m, cov=C)
    scipy_logpdf = rv.logpdf(X)

    print("NumPy realisation:")
    print(my_logpdf)

    print("\nScipy realisation:")
    print(scipy_logpdf)

    print("\nDifference:")
    print(my_logpdf - scipy_logpdf)


def task_6():
    a = np.arange(16).reshape(4, 4)
    print(f"Before:\n{a}")

    a[[1, 3]] = a[[3, 1]]

    print(f"After changing rows 1, 3: {a}")
    print(a)


def task_7():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')

    species_column = iris[:, -1]

    unique_species, counts = np.unique(species_column, return_counts=True)

    for name, count in zip(unique_species, counts):
        print(f"{name.decode() if isinstance(name, bytes) else name}: {count}")


def task_8():
    a = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
    nonzero_indices = np.nonzero(a)[0]

    print("Non-zero elements indexes:", nonzero_indices)


task_1()