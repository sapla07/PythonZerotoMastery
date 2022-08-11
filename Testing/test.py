import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_Stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_Stuff2(self):
        test_param = 'jdfhakjfah'
        result = main.do_stuff(test_param)
        # or self.assertIsInstance(result, ValueError)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_Stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
    unittest.main()
