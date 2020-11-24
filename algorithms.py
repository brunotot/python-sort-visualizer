import enum


class Algorithms(enum.Enum):
    QUICK_SORT = "Quick sort"
    SELECTION_SORT = "Selection sort"
    BUBBLE_SORT = "Bubble sort"
    MERGE_SORT = "Merge sort"
    HEAP_SORT = "Heap sort"
    RADIX_SORT = "Radix sort"

    @staticmethod
    def get(val):
        if val == Algorithms.BUBBLE_SORT.value:
            return Algorithms.BUBBLE_SORT
        elif val == Algorithms.QUICK_SORT.value:
            return Algorithms.QUICK_SORT
        elif val == Algorithms.SELECTION_SORT.value:
            return Algorithms.SELECTION_SORT
        elif val == Algorithms.MERGE_SORT.value:
            return Algorithms.MERGE_SORT
        elif val == Algorithms.HEAP_SORT.value:
            return Algorithms.HEAP_SORT
        elif val == Algorithms.RADIX_SORT.value:
            return Algorithms.RADIX_SORT


def quick_sort(data, cb, l, r):
    if l >= r:
        return
    x = data[l]
    j = l
    for i in range(l + 1, r + 1):
        if data[i] <= x:
            j += 1
            data[j], data[i] = data[i], data[j]
        yield data
    data[l], data[j] = data[j], data[l]
    yield data

    yield from quick_sort(data, cb, l, j - 1)
    yield from quick_sort(data, cb, j + 1, r)
    cb()


def selection_sort(data, cb):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]
        yield data
    cb()


def bubble_sort(data, cb):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data
    cb()


def merge_sort(data, cb):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data
    cb()


def heap_sort(data, cb):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data
    cb()


def radix_sort(data, cb):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data
    cb()


def get_ref(algorithm, data, cb):
    if algorithm == Algorithms.BUBBLE_SORT:
        return bubble_sort(data, cb)
    elif algorithm == Algorithms.QUICK_SORT:
        return quick_sort(data, cb, 0, len(data) - 1)
    elif algorithm == Algorithms.SELECTION_SORT:
        return selection_sort(data, cb)
    elif algorithm == Algorithms.MERGE_SORT:
        return merge_sort(data, cb)
    elif algorithm == Algorithms.HEAP_SORT:
        return merge_sort(data, cb)
    elif algorithm == Algorithms.RADIX_SORT:
        return merge_sort(data, cb)
