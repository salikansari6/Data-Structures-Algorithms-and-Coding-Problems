class Recursion:
    @staticmethod
    def count_down(num):
        if num <=0:
            print('done')
            return
        print(num)
        num -= 1
        Recursion.count_down(num)


if __name__ == '__main__':
    Recursion.count_down(4)