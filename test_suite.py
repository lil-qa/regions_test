import unittest

from tests.test_total_elements import TestTotalElements
from tests.test_page_size import TestPageSize
from tests.test_country_code import TestCountryCode
from tests.test_region_search import TestRegionSearch
from tests.test_pagination import TestPagination
from tests.test_combined import TestCombined

if __name__ == '__main__':
    loader = unittest.TestLoader()

    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestTotalElements))
    suite.addTests(loader.loadTestsFromTestCase(TestPageSize))
    suite.addTests(loader.loadTestsFromTestCase(TestCountryCode))
    suite.addTests(loader.loadTestsFromTestCase(TestRegionSearch))
    suite.addTests(loader.loadTestsFromTestCase(TestPagination))
    suite.addTests(loader.loadTestsFromTestCase(TestCombined))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
