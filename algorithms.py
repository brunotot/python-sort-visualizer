import enum
from all_algorithms.bubble import BubbleSort
from all_algorithms.heap import HeapSort
from all_algorithms.merge import MergeSort
from all_algorithms.quick import QuickSort
from all_algorithms.radix import RadixSort
from all_algorithms.selection import SelectionSort


class Algorithms(enum.Enum):
    QUICK_SORT = "Quick sort"
    SELECTION_SORT = "Selection sort"
    BUBBLE_SORT = "Bubble sort"
    MERGE_SORT = "Merge sort"
    HEAP_SORT = "Heap sort"
    RADIX_SORT = "Radix sort"

    @staticmethod
    def reference(algorithm, data):
        if algorithm == Algorithms.BUBBLE_SORT:
            return BubbleSort.get_reference(data)
        elif algorithm == Algorithms.QUICK_SORT:
            return QuickSort.get_reference(data)
        elif algorithm == Algorithms.SELECTION_SORT:
            return SelectionSort.get_reference(data)
        elif algorithm == Algorithms.MERGE_SORT:
            return MergeSort.get_reference(data)
        elif algorithm == Algorithms.HEAP_SORT:
            return HeapSort.get_reference(data)
        elif algorithm == Algorithms.RADIX_SORT:
            return RadixSort.get_reference(data)
