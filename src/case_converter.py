def convert_from_snake_to_camel_case(snake_case: str) -> str:
    words_list = snake_case.split("_")
    return words_list[0] + "".join([word.capitalize() for word in words_list[-1:]])


def convert_from_snake_to_kebab_case(snake_case: str) -> str:
    words_list = snake_case.split("_")
    return "-".join([word for word in words_list])
