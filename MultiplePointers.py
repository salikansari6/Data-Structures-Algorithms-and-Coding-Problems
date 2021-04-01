class MultiplePointers:
    @staticmethod
    def sumZero(arr):
        arr.sort()
        low = 0
        high = len(arr)-1
        while low<high:
            sum = arr[low]+arr[high]
            if sum == 0:
                return [arr[low], arr[high]]
            elif sum > 0:
                high -= 1
            else:
                low += 1


if __name__ == '__main__':
    print(MultiplePointers.sumZero([-4,-3,-2,-1,0,2,5]))