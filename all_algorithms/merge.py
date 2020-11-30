class MergeSort:
    @classmethod
    def get_reference(cls, data):
        return cls._merge_sort(data, 0, len(data)-1)

    @classmethod
    def _merge_sort(cls, A, start, end):
        if end <= start:
            return
        mid = start + ((end - start + 1) // 2) - 1
        yield from cls._merge_sort(A, start, mid)
        yield from cls._merge_sort(A, mid + 1, end)
        yield from cls._merge(A, start, mid, end)

    @classmethod
    def _merge(cls, A, start, mid, end):
        merged = []
        leftIdx = start
        rightIdx = mid + 1
        while leftIdx <= mid and rightIdx <= end:
            yield A
            if A[leftIdx] < A[rightIdx]:
                merged.append(A[leftIdx])
                leftIdx += 1
            else:
                merged.append(A[rightIdx])
                rightIdx += 1
        while leftIdx <= mid:
            yield A
            merged.append(A[leftIdx])
            leftIdx += 1
        while rightIdx <= end:
            yield A
            merged.append(A[rightIdx])
            rightIdx += 1
        for i in range(len(merged)):
            A[start + i] = merged[i]
            yield A 
