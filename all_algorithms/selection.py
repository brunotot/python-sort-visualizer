class SelectionSort:
    @classmethod
    def get_reference(cls, data):
        return cls._selection_sort(data)

    @classmethod
    def _selection_sort(cls, data):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, len(data)):
                yield data
                if data[min_idx] > data[j]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            yield data

