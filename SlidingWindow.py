class SlidingWindow:
    @staticmethod
    def max_sub_array_sum(arr, num):
        max_sum = 0
        temp_sum = 0
        if len(arr) < num:
            return None
        for i in range(0, num):
            max_sum += arr[i]
        temp_sum = max_sum
        for i in range(num, len(arr)):
            temp_sum = temp_sum - arr[i - num] + arr[i]
            max_sum = max(max_sum, temp_sum)
        return max_sum


if __name__ == '__main__':
    print(SlidingWindow.max_sub_array_sum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3))
