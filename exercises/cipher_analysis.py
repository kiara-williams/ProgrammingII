"""Script that takes in ciphertext and returns letter frequency for basic cryptanalysis"""
cipher_file = 'ciphertext.txt'
file = open(cipher_file, 'r')
count_dict = {}
char_count = 0
for line in file:
    for char in line:
        if char == ' ':
            pass
        elif char in count_dict:
            old_value = count_dict[char]
            new_value = old_value + 1
            count_dict[char] = new_value
            char_count += 1
        else:
            count_dict[char] = 1
            char_count += 1
file.close()
for char in count_dict:
    value = count_dict[char]
    percent = 100*(value/char_count)
    print("{} - {:.2f}%".format(char, percent))
