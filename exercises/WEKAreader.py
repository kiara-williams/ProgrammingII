LOOPSTOP = "<=>"

def main():
    attributes = {}
    attribute_list = []
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
    for key in attributes:
        print('{} = {}'.format(key, attributes[key]))
    in_file.close()

main()

