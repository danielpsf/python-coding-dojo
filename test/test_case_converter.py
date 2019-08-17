import unittest

from parameterized import parameterized
from sure import expect

from src.case_converter import convert_from_snake_to_camel_case


class CaseConverterTestCase(unittest.TestCase):

    @parameterized.expand([
        (
                'Should convert mashed_potato to mashedPotato',
                'mashed_potato',
                'mashedPotato',
        ),
        (
                'Should convert fried_potato to friedPotato',
                'fried_potato',
                'friedPotato',
        ),
        (
                'Should convert cooked_potato to cookedPotato',
                'cooked_potato',
                'cookedPotato',
        )
    ])
    def test_convert_from_snake_case_to_camel_case(self, name, snake_case, camel_case):
        expect(convert_from_snake_to_camel_case(snake_case)).equal_to(camel_case)


if __name__ == '__main__':
    unittest.main()
