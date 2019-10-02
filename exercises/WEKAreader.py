"""WEKA Reader for J48 tree - Kiara Williams
Takes tree as txt file and returns attribute count in order of significance.
Download WEKAfile.txt for a demonstration.
I hate it slightly less now."""

import operator

FILE = 'WEKAfile.txt'


def main():
    attributes = {}
    in_file = open(FILE, 'r')
    for line in in_file:
        line = line.replace("|", '')
        line = line.strip()
        try:
            current_attribute, waste = line.split('<=')
        except:
            try:
                current_attribute, waste = line.split('<')
            except:
                try:
                    current_attribute, waste = line.split('>')
                except:
                    try:
                        current_attribute, waste = line.split('>=')
                    except:
                        break
        if current_attribute in attributes:
            attributes[current_attribute] += 1
        else:
            attributes[current_attribute] = 1
    attributes = dict(sorted(attributes.items(), key=operator.itemgetter(1), reverse=True))
    for key in attributes:
        print('{} = {}'.format(key, attributes[key]))
    in_file.close()

main()

