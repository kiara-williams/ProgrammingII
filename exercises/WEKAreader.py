"""WEKA Reader for J48 Pre-formatted tree. I hate it too."""

import operator

def main():
    attributes = {}
    in_file = open('WEKAmodel.txt', 'r')
    for line in in_file:
        line.strip()
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

