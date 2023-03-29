def is_palindrome_recursive(word, low_index=None, high_index=None):
    if word is None or len(word) == 0 or not word:
        return False

    if low_index is None and high_index is None:  # Primeira chamada da função
        low_index, high_index = 0, len(word) - 1

    # Base da recursão: a palavra foi percorrida completamente
    if low_index >= high_index:
        return True

    # Se os caracteres nas pontas são diferentes, não é palíndromo
    if word[low_index] != word[high_index]:
        return False

    # Chamada recursiva para o próximo par de caracteres
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
