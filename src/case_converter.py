def convert_from_snake_to_camel_case(snake_case: str) -> str:
    words_list = snake_case.split("_")
    return words_list[0] + "".join([word.capitalize() for word in words_list[1:]])


def convert_from_snake_to_kebab_case(snake_case: str) -> str:
    words_list = snake_case.split("_")
    return "-".join([word for word in words_list])


def convert_from_camel_case_to_snake_case(camel_case: str) -> str:
    snake_case = ""
    for i in range(len(camel_case)):
        if camel_case[i].isupper():
            snake_case += "_" + camel_case[i:i+1].lower()
        else:
            snake_case += camel_case[i]

    return snake_case
