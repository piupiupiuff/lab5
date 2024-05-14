import random
import time

def generate_array(length):
    return [random.randint(0, 10000) for _ in range(length)]

def sort(arr):
    comparisons = 0
    swaps = 0
    start_time = time.time()

    if len(arr) <= 1:
        return arr, comparisons, swaps, time.time() - start_time
    else:
        p = arr[0]
        less_than_p = [x for x in arr[1:] if x <= p]
        greater_than_p = [x for x in arr[1:] if x > p]
        comparisons += len(arr) - 1
        swaps += len(arr) - 1
        sorted_less, comparisons_less, swaps_less, time_less = sort(less_than_p)
        sorted_greater, comparisons_greater, swaps_greater, time_greater = sort(greater_than_p)
        return sorted_less + [p] + sorted_greater, comparisons + comparisons_less + comparisons_greater, swaps + swaps_less + swaps_greater, time.time() - start_time


arr_100 = generate_array(100)
arr_1000 = generate_array(1000)
arr_10000 = generate_array(10000)


sorted_arr_100, comparisons_100, swaps_100, time_100 = sort(arr_100)
sorted_arr_1000, comparisons_1000, swaps_1000, time_1000 = sort(arr_1000)
sorted_arr_10000, comparisons_10000, swaps_10000, time_10000 = sort(arr_10000)

print("Для масиву з 100 елементами:")
print("Кількість порівнянь:", comparisons_100)
print("Кількість обмінів:", swaps_100)
print("Час роботи:", time_100)

print("Для масиву з 1000 елементами:")
print("Кількість порівнянь:", comparisons_1000)
print("Кількість обмінів:", swaps_1000)
print("Час роботи:", time_1000)

print("Для масиву з 10000 елементами:")
print("Кількість порівнянь:", comparisons_10000)
print("Кількість обмінів:", swaps_10000)
print("Час роботи:", time_10000)
