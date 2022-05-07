input_str = input()
set_of_symbols = set(input_str)
counts_of_words = [(input_str.count(sym), sym) for sym in set_of_symbols]
value = max(counts_of_words)[0]
counts_of_words_with_len = [elem for elem in counts_of_words if elem[0] == value]
print(min(counts_of_words_with_len))
