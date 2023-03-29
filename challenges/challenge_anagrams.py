def is_anagram(first_string, second_string):
    if not first_string \
            or not second_string \
            or len(first_string) < 2 \
            or len(second_string) < 2:
        return (first_string, second_string, False)
