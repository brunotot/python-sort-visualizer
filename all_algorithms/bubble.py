class BubbleSort:
    @classmethod
    def get_reference(cls, data):
        return cls._bubble_sort(data)

    @classmethod
    def _bubble_sort(cls, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    yield data
                else:
                    yield data
