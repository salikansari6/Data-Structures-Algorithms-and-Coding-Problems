class Recursion:
    @staticmethod
    def count_down(num):
        if num <= 0:
            print('done')
            return
        print(num)
        num -= 1
        Recursion.count_down(num)

    @staticmethod
    def sum_range(num):
        if num == 1:
            return 1
        return num + Recursion.sum_range(num-1)

    @staticmethod
    def factorial(num):
        if num == 0:
            return 0
        if num == 1 or num == 2:
            return num
        return num * Recursion.factorial(num-1)


if __name__ == '__main__':
    # Recursion.count_down(4)
    # print(Recursion.sum_range(4))
    print(Recursion.factorial(3))