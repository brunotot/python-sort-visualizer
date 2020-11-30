class RadixSort:
    @classmethod
    def get_reference(cls, data):
        return cls._radix_sort(data)

    @classmethod
    def _counting_sort(cls, arr, exp1):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(0, n):
            yield arr
            index = (arr[i] / exp1)
            count[int(index % 10)] += 1

        for i in range(1, 10):
            yield arr
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            yield arr
            index = (arr[i] / exp1)
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
            yield arr

    @classmethod
    def _radix_sort(cls, arr):
        max1 = max(arr)
        exp = 1
        while max1 // exp > 0:
            print(max1)
            yield from cls._counting_sort(arr, exp)
            exp *= 10
