"""Exercise (Measure Time):
@measure_time
def binary_search(lst_sorted, value):

while len(lst_sorted) > 1:
    print(step)
    middle = len(lst_sorted) // 2
    if lst_sorted[middle] != value:
        if lst_sorted[middle] > value:
            lst_sorted = lst_sorted[:middle]
        elif lst_sorted[middle] < value:
            lst_sorted = lst_sorted[middle:]
    else:
        return True
return False 
Write a decorator measure_time which measures how long the function takes.
mesure the time for X = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
plot the time against X


1:03
Hint: the inner function of decorator should return the time only."""

# Solution 1
import timeit
import matplotlib.pyplot as plt

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return execution_time
    return wrapper

#@measure_time
def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False

X = range(1, 1001)
X = [num for num in X if num % 4 == 0]

execution_times = []

for x in X:
    lst_sorted = list(range(x))
    execution_time = timeit.timeit(lambda: binary_search(lst_sorted, x-1), number=1)
    execution_times.append(execution_time)

plt.plot(X, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()


print("_________________________________________________")

# Solution 2
"""import timeit
import matplotlib.pyplot as plt

def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False

X = range(1, 1001)
X = [num for num in X if num % 4 == 0]
#X = [100, 10_000, 100_000, 1_000_000]
execution_times = []

for x in X:
    lst_sorted = list(range(x))
    execution_time = timeit.timeit(lambda: binary_search(lst_sorted, x-1), number=1)
    execution_times.append(execution_time)

plt.plot(X, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()
"""
print("_____________________________________________")

# Solution
"""import timeit
import matplotlib.pyplot as plt
import numpy as np

def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False

X = range(1, 1001)
X = [num for num in X if num % 4 == 0]
#X = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
execution_times = []

for x in X:
    lst_sorted = list(range(x))
    execution_time = timeit.timeit(lambda: binary_search(lst_sorted, x-1), number=1)
    execution_times.append(execution_time)

plt.plot(X, execution_times, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()"""

print("_________________________________________")

# Solution again
"""import timeit
import matplotlib.pyplot as plt

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return execution_time
    return wrapper

@measure_time
def binary_search(lst_sorted, value):
    while len(lst_sorted) > 1:
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False

X = [num for num in range(1, 1001) if num % 4 == 0]
execution_times = []

for x in X:
    lst_sorted = list(range(x))
    execution_time = timeit.timeit(lambda: binary_search(lst_sorted, x-1), number=1)
    execution_times.append(execution_time)

plt.plot(X, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Binary Search Execution Time')
plt.show()"""

