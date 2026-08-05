

def convert_tuple(data: str) -> tuple:
    converter = []
    result = []

    converter.append(data)
    result.append(tuple(converter))

    return result[0]

def convert_tuple_many(data_list: list) -> list:
    converter = []
    result = []

    i = 0
    for item in data_list:
        converter.append(data_list[i])
        result.append(tuple(converter))
        converter.clear()
        i = i + 1

    return result