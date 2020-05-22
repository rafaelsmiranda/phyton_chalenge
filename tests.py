import unittest

from footer import pagination


class FooterTests(unittest.TestCase):
    def _init_(self, testName):
        super(FooterTests, self)._init_(testName)

    def pagination_default(self):
        '''Default values should work'''
        self.assertEqual(pagination(), "1 ... 10")

    def pagination_current_page_should_not_exceeed_total_number_of_pages(self):
        '''Current page should not exceed total number of pages'''
        self.assertEqual(
            pagination(5, 2, 0, 0), "Current page exceeds total number of pages")

    def pagination_exercise_example_1(self):
        '''Values from exercise example 1 should work'''
        self.assertEqual(pagination(4, 5, 1, 0), "1 ... 4 5")

    def pagination_exercise_example_2(self):
        '''Values from exercise example 2 should work'''
        self.assertEqual(pagination(4, 10, 2, 2), "1 2 3 4 5 6 ... 9 10")

    def pagination_high_boundaries_value_should_not_break(self):
        '''High boundaries value should not break'''
        self.assertEqual(pagination(5, 10, 20, 0), "1 2 3 4 5 6 7 8 9 10")


suite = unittest.TestSuite()
suite.addTest(FooterTests("pagination_default"))
suite.addTest(FooterTests(
    "pagination_current_page_should_not_exceeed_total_number_of_pages"))
suite.addTest(FooterTests("pagination_exercise_example_1"))
suite.addTest(FooterTests("pagination_exercise_example_2"))
suite.addTest(FooterTests("pagination_exercise_example_2"))
unittest.TextTestRunner(verbosity=2).run(suite)
