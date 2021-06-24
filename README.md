# QuickSortTest

This is a readme to test the existing Quicksort methods with different partioning techniques for Quicksort1, quicksort2, quicksort3 and quicksort4

---

## Instructions to build and run
* Clone the repository using the command
  git clone [https://github.com/abirami91/quicksortTest.py.git]

* Checkout on the main Directory

* To be able to run the tests plese install pytest based on your IDE using the command
  pip install pytest

* Run the test using following command
  pytest testQuickSortList.py

* To be able to generate the report in html, use the following command
  pytest testQuickSortList.py --html=report.html

---

---
##Insights of the .py files
* quicksort.py contains the four different algorithms to test
   1. Quicksort1 with its partition1 to get pivot
   2. Quicksort2 with its partition2 to get pivot 
   3. Quicksort3 with its partition3 to get pivot
   4. Quicksort4 with its partition4 to get pivot
   5. And an array of all the quicksorts from above

* testQuickSortList.py contains a pytest based parameterized unit test methods to evaluate all the methods from quicksort. The tests are based on the following
   1. Inputs with random list of 250 range
   2. Inputs with random list without duplicates
   3. Inputs with partially sorted lists
   4. Inputs with reversely sorted list
   5. Inputs with negative list
   Based on several tests, Quicksort4 seems to be more stable, please refer to the html report to have a look at failed and passed test cases

* performanceQuickSort.py contains the time that each algorithm takes to execute, it also contains the comparison between sorted algorithm with all the four quicksort algorithm

---