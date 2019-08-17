import unittest

from parameterized import parameterized
from sure import expect

from src.case_converter import convert_from_snake_to_camel_case, convert_from_snake_to_kebab_case


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
                'Should convert backed_potato to bakedPotato',
                'baked_potato',
                'bakedPotato',
        )
    ])
    def test_convert_from_snake_case_to_camel_case(self, name, snake_case, camel_case):
        expect(convert_from_snake_to_camel_case(snake_case)).equal_to(camel_case)

    @parameterized.expand([
        (
                'Should convert mashed_potato to mashed-potato',
                'mashed_potato',
                'mashed-potato',
        ),
        (
                'Should convert fried_potato to fried-potato',
                'fried_potato',
                'fried-potato',
        ),
        (
                'Should convert backed_potato to baked-potato',
                'baked_potato',
                'baked-potato',
        )
    ])
    def test_convert_from_snake_case_to_kebab_case(self, name, snake_case, kebab_case):
        expect(convert_from_snake_to_kebab_case(snake_case)).equal_to(kebab_case)


if __name__ == '__main__':
    unittest.main()
