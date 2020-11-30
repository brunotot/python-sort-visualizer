class QuickSort:
    @classmethod
    def get_reference(cls, data):
        return cls._quick_sort(data, 0, len(data) - 1)

    @classmethod
    def _quick_sort(cls, data, l, r):
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
        yield from cls._quick_sort(data, l, j - 1)
        yield from cls._quick_sort(data, j + 1, r)
