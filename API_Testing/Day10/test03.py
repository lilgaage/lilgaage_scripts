import unittest
import ddt

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@ddt.ddt()
class Print(unittest.TestCase):
    @ddt.data(*list_num)
    def test_print(self, number):
        print("打印的数字是：{}".format(number))


if __name__ == '__main__':
    unittest.main()

