import unittest


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self) :
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @unittest.SkipTest
    def test_search(self):
        print("This is a search test")

    @unittest.skip("I am skipping this mehtod becauze it is not yet ready")
    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is a prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is a postpaid Recharge test")

if __name__ == "__main__":
    unittest.main()
