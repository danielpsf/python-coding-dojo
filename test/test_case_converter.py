import unittest

from parameterized import parameterized
from sure import expect

from src.case_converter import convert_from_snake_to_camel_case, convert_from_snake_to_kebab_case, \
    convert_from_camel_case_to_snake_case


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
        ),
        (
                'Should convert baked_potato_with_cream_cheese to bakedPotatoWithCreamCheese',
                'baked_potato_with_cream_cheese',
                'bakedPotatoWithCreamCheese',
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
        ),
        (
                'Should convert baked_potato_with_cream_cheese to baked-potato-with-cream-cheese',
                'baked_potato_with_cream_cheese',
                'baked-potato-with-cream-cheese',
        )
    ])
    def test_convert_from_snake_case_to_kebab_case(self, name, snake_case, kebab_case):
        expect(convert_from_snake_to_kebab_case(snake_case)).equal_to(kebab_case)

    @parameterized.expand([
        (
                'Should convert mashedPotato to mashed_potato',
                'mashedPotato',
                'mashed_potato',
        ),
        (
                'Should convert friedPotato to fried_potato',
                'friedPotato',
                'fried_potato',
        ),
        (
                'Should convert backedPotato to baked_potato',
                'bakedPotato',
                'baked_potato',
        ),
        (
                'Should convert bakedPotatoWithCreamCheese to baked_potato_with_cream_cheese',
                'bakedPotatoWithCreamCheese',
                'baked_potato_with_cream_cheese',
        )
    ])
    def test_convert_from_camel_case_to_snake_case(self, name, camel_case, snake_case):
        expect(convert_from_camel_case_to_snake_case(camel_case)).equal_to(snake_case)


if __name__ == '__main__':
    unittest.main()
