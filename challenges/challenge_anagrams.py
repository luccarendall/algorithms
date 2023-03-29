def sort_list(list):
    part_one = []
    part_two = []

    # Validação para evitar loop infinito
    if len(list) < 1:
        return list

    letters = 0
    while letters < len(list) - 1:
        # verifica se é menor do que o último elemento
        if list[letters] < list[-1]:
            part_one.append(list[letters])
        else:
            part_two.append(list[letters])
        letters += 1

    # Junta a primeira parte, o último elemento e a segunda parte
    return sort_list(part_one) + [list[-1]] + sort_list(part_two)


def is_anagram(first_list, second_list):
    if first_list is None \
            or len(first_list) == 0 \
            or not first_list \
            or second_list is None \
            or len(second_list) == 0 \
            or not second_list:
        return first_list, second_list, False

    # Converte listas para lower case
    list_one = list(first_list.lower())
    list_two = list(second_list.lower())

    # Ordena as listas usando o metodo sort_list
    list_sorted_one = sort_list(list_one)
    list_sorted_two = sort_list(list_two)

    # Verifica se as listas são anagramas
    if list_sorted_one == list_sorted_two:
        return ''.join(list_sorted_one), ''.join(list_sorted_two), True
    else:
        return ''.join(list_sorted_one), ''.join(list_sorted_two), False
