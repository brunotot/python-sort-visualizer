class HeapSort:
    @classmethod
    def get_reference(cls, data):
        return cls._heap_sort(data)

    @classmethod
    def _heapify(cls, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            yield arr
            yield from cls._heapify(arr, n, largest)

    @classmethod
    def _heap_sort(cls, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            yield from cls._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            yield arr
            yield from cls._heapify(arr, i, 0)
