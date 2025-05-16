# Escreva uma função que receba uma lista e retorne a mesma lista
# com os valores ordenados, mas mantendo os tipos originais no mesmo lugar
# Exemplo: ["b", 1, "a", 2] retorna ["a", 1, "b", 2]
def sort_by_type(mixed_list):
    strings = sorted([x for x in mixed_list if isinstance(x, str)])
    integers = sorted([x for x in mixed_list if isinstance(x, int)])

    result = []
    str_index = 0
    int_index = 0

    for item in mixed_list:
        if isinstance(item, str):
            result.append(strings[str_index])
            str_index += 1
        elif isinstance(item, int):
            result.append(integers[int_index])
            int_index += 1

    return result


def main():
    to_sort = [1, "c", 5, 6, 2, "t", "h", "i", "a"]
    print(sort_by_type(to_sort))
    

if __name__ == "__main__":
    main()

