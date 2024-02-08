def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example:
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print(reversed_sentence)