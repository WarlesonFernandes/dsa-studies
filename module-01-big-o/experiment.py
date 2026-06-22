import timeit
import random

# Expeiment setup: sizes to teste the growth of O(N) vs O(log N)
INPUT_SIZES = [1000, 10000, 100000, 1000000, 10000000, 100000000]

def linear_search(data, target):
    #O(N) - Linear Search: visits every element.
    for item in data:
        if item == target:
            return True
    return False

def binary_search(data, target):
    # O(log N)- Binary Search: divedes search space in half.
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return False

def run_benchmark():
    print(f"{'Input Size':<12} | {'Linear Search (s)':<18} | {'Binary Search (s)':<18}")
    print("-" * 55)

    for n in INPUT_SIZES:
        # Preparing the data
        data = sorted(list(range(n)))
        target = n-1 # Worst case: target is at the very end

        # Benchmarking (running 100 times for a stable average)
        time_linear = timeit.timeit(lambda: linear_search(data, target), number = 100)
        time_binary = timeit.timeit(lambda: binary_search(data, target), number =100)
        
        print(f"{n:<12} | {time_linear:<18.6f} | {time_binary:<18.6f}")

if __name__ == "__main__":
    run_benchmark()

