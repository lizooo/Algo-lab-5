def rabin_karp(text, pattern, radix_d, modulo_prime):
    text_len = len(text)
    pattern_len = len(pattern)
    pattern_hash = 0
    text_window_hash = 0
    coordinates_of_occurrences = []
    coordinates_of_occurrences_to_test = []
    for symbol_index in range(pattern_len):
        pattern_hash = (radix_d * pattern_hash + ord(pattern[symbol_index])) % modulo_prime
        text_window_hash = (radix_d * text_window_hash + ord(text[symbol_index])) % modulo_prime
    for window_index in range(text_len - pattern_len + 1):
        if pattern_hash == text_window_hash:
            symbol_index = check_symbol_by_symbol(pattern, pattern_len, symbol_index, text, window_index)
            if symbol_index == pattern_len:
                coordinates_of_occurrences.append(f'({window_index}, {window_index + pattern_len - 1})')
                coordinates_of_occurrences_to_test.append((window_index, window_index + pattern_len - 1))
        if window_index < text_len - pattern_len:
            text_window_hash = (radix_d * (text_window_hash - ord(text[window_index]) *
                                           (pow(radix_d, pattern_len - 1)) % modulo_prime) +
                                ord(text[window_index + pattern_len])) % modulo_prime
    with open("output.txt", "w") as output_file:
        for item in coordinates_of_occurrences:
            output_file.write("%s\n" % item)

    return coordinates_of_occurrences_to_test


def check_symbol_by_symbol(pattern, pattern_len, symbol_index, text, window_index):
    for symbol_index in range(pattern_len):
        if pattern[symbol_index] != text[window_index + symbol_index]:
            break
        else:
            symbol_index += 1
    return symbol_index


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        text_from_input, pattern_from_input = [line.rstrip() for line in input_file]
    rabin_karp(text_from_input, pattern_from_input, 256, 1000007)

