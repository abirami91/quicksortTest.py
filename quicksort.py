import pytest


def swap(l, f, s):
    l[f], l[s] = l[s], l[f]


def partition1(input_list, pivot_index, start, end):
    swap(input_list, start, pivot_index)
    left = start + 1
    right = end - 1
    for current in range(start + 1, end):
        if current <= left:
            continue
        if current >= right:
            break
        if input_list[current] < input_list[start]:
            swap(input_list, current, left)
            left += 1
        else:
            swap(input_list, current, right)
            right -= 1

    swap(input_list, start, left)
    return left


def qsort1(input_list, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(input_list)
    if end - start <= 1:
        return

    pivot_index = start
    pivot_index = partition1(input_list, pivot_index, start, end)
    qsort1(input_list, start, pivot_index)
    qsort1(input_list, pivot_index + 1, end)


def partition2(input_list, pivot_index, start, end):
    swap(input_list, start, pivot_index)
    pivot = input_list[start]
    left = start
    right = end
    for current in range(start + 1, end):
        if current <= left:
            continue
        if current >= right:
            break
        if input_list[current] < pivot:
            left += 1
            swap(input_list, current, left)
        else:
            right -= 1
            swap(input_list, current, right)

    swap(input_list, start, left)
    return left


def qsort2(input_list, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(input_list)
    if end - start <= 1:
        return

    # pick a pivot
    pivot_index = start
    pivot_index = partition2(input_list, pivot_index, start, end)
    # partition on the pivot
    # qsort the two subranges
    qsort2(input_list, start, pivot_index)
    qsort2(input_list, pivot_index + 1, end)
    return input_list


def partition3(input_list, pivot_index, start, end):
    swap(input_list, start, pivot_index)
    pivot = input_list[start]
    left = start
    right = end
    for current in range(start + 1, end):
        if current <= left:
            continue
        if current >= right:
            break
        if input_list[current] <= pivot:
            left += 1
            swap(input_list, current, left)
        else:
            right -= 1
            swap(input_list, current, right)

    swap(input_list, start, left)
    return left


def qsort3(input_list, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(input_list)
    if end - start <= 1:
        return

    # pick a pivot
    pivot_index = start
    pivot_index = partition3(input_list, pivot_index, start, end)
    # partition on the pivot
    # qsort the two subranges
    qsort3(input_list, start, pivot_index)
    qsort3(input_list, pivot_index + 1, end)
    return input_list


def partition4(input_list, start, end):
    pivot = input_list[end - 1]
    left = start - 1
    right = end - 1
    for current in range(start, end):
        if current <= left:
            continue
        if current >= right:
            break
        if input_list[current] <= pivot:
            left += 1
            swap(input_list, current, left)

    swap(input_list, end - 1, left + 1)
    return left + 1


def qsort4(input_list, start=None, end=None):
    if start == None:
        start = 0
    if end == None:
        end = len(input_list)
    if end - start <= 1:
        return input_list

    # pick a pivot
    pivot_index = partition4(input_list, start, end)
    # partition on the pivot
    # qsort the two subranges
    qsort4(input_list, start, pivot_index)
    qsort4(input_list, pivot_index + 1, end)
    return input_list


def obviously_wrong(input):
    return input


sorts = [qsort1, qsort2, qsort3, qsort4]
sorts_function_Name = ["QuickSort1", "QuickSort2", "QuickSort3", "QuickSort4"]
