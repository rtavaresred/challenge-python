def analyze_unusual_words(word_list: list[str], start_index: int, end_index: int) -> dict:
    """
    DOCSTRING:
    Analisa um intervalo de palavras de uma lista e retorna estatísticas sobre elas.
    Conta quantas palavras são longas (mais de 8 letras), curtas (menos de 5 letras)
    e identifica a palavra mais longa do intervalo.

    EXEMPLO:
    >>> analyze_unusual_words(["apple", "encyclopedia", "bat", "neighborhood", "sky"], 1, 4)
    {'long_words': 2, 'short_words': 1, 'longest_word': 'neighborhood'}
    """
    start_index = max(0, min(start_index, len(word_list) - 1))
    end_index = max(0, min(end_index, len(word_list) - 1))
    
    subset = word_list[start_index:end_index + 1]
    
    long_words = 0
    short_words = 0
    longest_word = ""
    
    for word in subset:
        if len(word) > 8:
            long_words += 1
        elif len(word) < 5:
            short_words += 1
        
        if len(word) > len(longest_word):
            longest_word = word
    
    return {
        'long_words': long_words,
        'short_words': short_words,
        'longest_word': longest_word
    }

print(analyze_unusual_words(['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij'], 0, 9))