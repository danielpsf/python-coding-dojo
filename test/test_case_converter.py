import unittest

from parameterized import parameterized
from sure import expect

from src.case_converter import convert_from_snake_to_camel_case


class CaseConverterTestCase(unittest.TestCase):

    @parameterized.expand([
        (
                'Should convert potato_name to potatoName',
                'potato_name',
                'potatoName',
        )
    ])
    def test_convert_from_snake_case_to_camel_case(self, name, snake_case, camel_case):
        expect(convert_from_snake_to_camel_case(snake_case)).equal_to(camel_case)


if __name__ == '__main__':
    unittest.main()
