def Rabin_Karp(text, pattern, shift_value, prime_number):
    text_len = len(text)
    pattern_len = len(pattern)
    pattern_hash = 0
    text_window_hash = 0
    coordinates_of_occurrences = []
    for symbol_index in range(pattern_len):
        pattern_hash = (shift_value * pattern_hash + ord(pattern[symbol_index])) % prime_number
        text_window_hash= (shift_value * text_window_hash + ord(text[symbol_index])) % prime_number
    for window_index in range(text_len - pattern_len + 1):
        if pattern_hash == text_window_hash:
            for symbol_index in range(pattern_len):
                if pattern[symbol_index] != text[window_index + symbol_index]:
                    continue
            coordinates_of_occurrences.append((window_index, window_index + pattern_len-1))
        if window_index < text_len - pattern_len:
            text_window_hash = (shift_value * (text_window_hash - ord(text[window_index]) * (pow(shift_value, pattern_len - 1) % prime_number)) + ord(text[window_index + pattern_len])) % prime_number

    return coordinates_of_occurrences

#todo add reader and writers


print(Rabin_Karp("abjskwihwabasbmw", "ab", 257, 11))
print(Rabin_Karp("xxxxx", "xx", 40999999, 999999937))

