# The below method is used for estimating the time consumed by the quicksort algorithms
import timeit
import random

import quicksort


def evaluatePerformance():
    list_no = [3, 8, 1, 9, 12, 2, 11, 7, 5, 4]
    print('Not sorted: %s' % list_no)
    print('Sorted quicksort1: %s' % quicksort.qsort1(list_no, 0, len(list_no) - 1))
    print('Sorted quicksort2: %s' % quicksort.qsort2(list_no, 0, len(list_no) - 1))
    print('Sorted quicksort3: %s' % quicksort.qsort3(list_no, 0, len(list_no) - 1))
    print('Sorted quicksort4: %s' % quicksort.qsort4(list_no, 0, len(list_no) - 1))

    # Comparison between quick sort (both with pivot as the first element and random pivot) and the built-in Python sort
    random_list = [random.random() for _ in range(10000)]
    t1qs1 = timeit.Timer(lambda: quicksort.qsort1(random_list, 0, len(random_list) - 1)).timeit(number=1)
    t1qs2 = timeit.Timer(lambda: quicksort.qsort2(random_list, 0, len(random_list) - 1)).timeit(number=1)
    t1qs3 = timeit.Timer(lambda: quicksort.qsort3(random_list, 0, len(random_list) - 1)).timeit(number=1)
    t1qs4 = timeit.Timer(lambda: quicksort.qsort4(random_list, 0, len(random_list) - 1)).timeit(number=1)
    random_list2 = [random.random() for _ in range(10000)]
    t3 = timeit.Timer(lambda: sorted(random_list2)).timeit(number=1)
    print('Time to sort 250 ints with quick sort1 (first element as pivot): %f seconds' % t1qs1)
    print('Time to sort 250 ints with quick sort2 (first element as pivot): %f seconds' % t1qs2)
    print('Time to sort 250 ints with quick sort3 (first element as pivot): %f seconds' % t1qs3)
    print('Time to sort 250 ints with quick sort4 (first element as pivot): %f seconds' % t1qs4)
    print('Time to sort 250 ints with python built-in sort : %f seconds' % t3)
    print('1quicksort/built-in: %f' % (t1qs1 / t3))
    print('2quicksort/built-in: %f' % (t1qs2 / t3))
    print('3quicksort/built-in: %f' % (t1qs3 / t3))
    print('4quicksort/built-in: %f' % (t1qs4 / t3))
