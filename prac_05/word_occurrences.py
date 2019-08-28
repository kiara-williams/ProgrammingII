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
    print(words)


main()