import unittest
import ret


class Test(unittest.TestCase):
    """A class that has a unit test"""
    def test_base(self):
        """Function comparing data from both tables"""
        a = ret.check_work()
        b = ret.check_employees()
        l = len(a)
        for i in range(l):
            self.assertEqual(a[i], b[i])


if __name__ == '__main__':
    unittest.main()
