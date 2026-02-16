def analyze_sentence(sentence):
    """
    Analyzes a sentence ending with a period.
    
    Args:
        sentence (str): A string that ends with a period.
    
    Returns:
        tuple: (char_count, word_count, vowel_count)
    """
    char_count = 0
    word_count = 0
    vowel_count = 0
    vowels = set('aeiouAEIOU')

    # Read character by character
    for ch in sentence:
        char_count += 1
        if ch in vowels:
            vowel_count += 1
        if ch == ' ':
            word_count += 1
        # Stop if we encounter a period (but we already counted it)
        if ch == '.':
            break

    # Number of words = spaces + 1 (assuming at least one word)
    total_words = word_count + 1

    return char_count, total_words, vowel_count

def main():
    # Example usage
    sentence = input("Enter a sentence ending with a period: ")
    length, words, vowels = analyze_sentence(sentence)
    print(f"\nResults:")
    print(f"Length of sentence (including period): {length}")
    print(f"Number of words: {words}")
    print(f"Number of vowels: {vowels}")

if __name__ == "__main__":
    main()