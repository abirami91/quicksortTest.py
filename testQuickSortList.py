import random
import pytest
import quicksort


# parameterized method for Quicksort1 to Quicksort4
# list of size 250 with values between 0 and 250 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_random_list_range250(quicksortfunction):
    random_list = []
    # with duplicates
    for i in range(0, 250):
        num_list = random.randint(1, 250)
        random_list.append(num_list)
    sorted_list = sorted(random_list)
    result_list = quicksortfunction(random_list)
    if result_list is None:
        assert False
    for j in range(0, 250):
        assert sorted_list[j] == result_list[j]
    print(str(quicksortfunction) + "Passed")


# parameterized method for Quicksort1 to Quicksort4
# list of size 100 with values between 0 and 100 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_random_list_range100(quicksortfunction):
    random_list = []
    # with duplicates
    for i in range(0, 100):
        num_list = random.randint(1, 100)
        random_list.append(num_list)
    sorted_list = sorted(random_list)
    result_list = quicksortfunction(random_list)
    if result_list is None:
        assert False
    for j in range(0, 100):
        assert sorted_list[j] == result_list[j]
    print(str(quicksortfunction) + "Passed")


# parameterized method for Quicksort1 to Quicksort4
# list of size 250 without duplicates and values between 0 and 250 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_without_duplicates_list_250(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(250), 250)
    sorted_list = sorted(randomlist_without_duplicates)
    result_list_sort1 = quicksortfunction(randomlist_without_duplicates)
    if result_list_sort1 is None:
        assert False
    for i in range(0, 250):
        assert sorted_list[i] == result_list_sort1[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 5 without duplicates and values between 0 and 5 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_without_duplicates_list_5(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(5), 5)
    sorted_list = sorted(randomlist_without_duplicates)
    result_list_sort2 = quicksortfunction(randomlist_without_duplicates)
    if result_list_sort2 is None:
        assert False
    for i in range(0, 5):
        assert sorted_list[i] == result_list_sort2[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 10 without duplicates and values between 0 and 10 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_without_duplicates_list_10(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(10), 10)
    sorted_list = sorted(randomlist_without_duplicates)
    result_list_sort3 = quicksortfunction(randomlist_without_duplicates)
    if result_list_sort3 is None:
        assert False
    for i in range(0, 10):
        assert sorted_list[i] == result_list_sort3[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 25 without duplicates and values between 0 and 25 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_without_duplicates_list_25(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(25), 25)
    sorted_list = sorted(randomlist_without_duplicates)
    result_list_sort2 = quicksortfunction(randomlist_without_duplicates)
    if result_list_sort2 is None:
        assert False
    for i in range(0, 25):
        assert sorted_list[i] == result_list_sort2[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 50 without duplicates and values between 0 and 50 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_without_duplicates_list_50(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(50), 50)
    sorted_list = sorted(randomlist_without_duplicates)
    result_list_sort3 = quicksortfunction(randomlist_without_duplicates)
    if result_list_sort3 is None:
        assert False
    for i in range(0, 50):
        assert sorted_list[i] == result_list_sort3[i]


# parameterized method for Quicksort1 to Quicksort4
# list of partially generated (half sorted half unsorted) of range 250 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_partially_sorted_list(quicksortfunction):
    randomlist = random.sample(range(250), 250)
    randomlist_sorted = sorted(randomlist)
    randomlist_temp_sorted = sorted(randomlist)
    for i in range(0, 25):
        random_index_1 = random.randint(0, 125)
        random_index_2 = random.randint(126, 249)
        randomlist_temp_sorted[random_index_1], randomlist_temp_sorted[random_index_2] = randomlist_temp_sorted[
                                                                                             random_index_2], \
                                                                                         randomlist_temp_sorted[
                                                                                             random_index_1]
    randomlist_partially_sorted = randomlist_temp_sorted
    result = quicksortfunction(randomlist_partially_sorted)
    if result is None:
        assert False
    for i in range(0, 250):
        assert randomlist_sorted[i] == result[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 250 with reversed sorted values between 0 and 250 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_reverse_sort_250(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(250), 250)
    randomlist_reversely_sorted = sorted(randomlist_without_duplicates, reverse=True)
    print(randomlist_reversely_sorted)
    result = quicksortfunction(randomlist_reversely_sorted)
    if result is None:
        assert False
    for i in range(0, 250):
        assert randomlist_reversely_sorted[i] == result[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 100 with reversed sorted values between 0 and 100 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_reverse_sort_100(quicksortfunction):
    randomlist_without_duplicates = random.sample(range(100), 100)
    randomlist_reversely_sorted = sorted(randomlist_without_duplicates, reverse=True)
    print(randomlist_reversely_sorted)
    result = quicksortfunction(randomlist_reversely_sorted)
    if result is None:
        assert False
    for i in range(0, 100):
        assert randomlist_reversely_sorted[i] == result[i]


# parameterized method for Quicksort1 to Quicksort4
# list of size 5 with negative sorted values between 0 and 100 is used as a test input
@pytest.mark.parametrize(
    'quicksortfunction',
    (quicksort.qsort1, quicksort.qsort2, quicksort.qsort3, quicksort.qsort4))
def test_negative_list_already_sorted(quicksortfunction):
    list_number = [1, 2, 3, -7]
    neglist = [-x for x in list_number]
    print(neglist)
    result = quicksortfunction(neglist)
    if result is None:
        assert False
    for i in range(0, 4):
        assert neglist[i] == result[i]
