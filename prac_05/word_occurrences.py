"""Program that takes a string and counts unique words"""

def main():
    words = {}
    longest_word = 0
    word_string = input("Enter a string").lower()
    word_list = word_string.split()
    for word in word_list:
        if len(word) > longest_word:
            longest_word = len(word)
        if word in words:
            """check if word in dict and modify value"""
            old_value = words[word]
            new_value = old_value + 1
            words[word] = new_value
        else:
            words[word] = 1
    print("Text: {}".format(word_string))
    print("{:<{}}     {}".format("Word", longest_word, "Count"))
    print("_________________________________")
    while len(words) > 0:
        """Sort dict while printing"""
        current_word = min(words)
        print("{:<{}}  :  {}".format(current_word, longest_word, words[current_word]))
        words.pop(current_word)


main()