def main():
    words = {}
    word_string = input("Enter a string")
    word_list = word_string.split()
    for word in word_list:
        if word in words:
            old_value = words[word]
            new_value = old_value + 1
            words[word] = new_value
        else:
            words[word] = 1
    while len(words) > 0:
        current_word = min(words)
        print(current_word, words[current_word])
        words.pop(current_word)


main()