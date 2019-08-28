"""Program that returns hex colour for string
Was undecided whether or not to use uppercase characters in dict. Chose not to for increased matches
with the input string."""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "blanchedalmond": "#ffebcd", "darkorchid": "9932cc", "dimgray": "#696969",
               "gainsboro": "#dcdcdc", "indianred": "#cd5c5c", "lawngreen": "#7cfc00", "mintcream": "#f5fffa",
               "oldlace": "#fdf5e6", "olivedrab": "#6b8e23", "palegoldenrod": "#eee8aa", "papayawhip": "#ffefd5",
               "rebeccapurple": "#663399", "saddlebrown": "#8b4513", "whitesmoke": "#f5f5f5"}

def main():
    colour_choice = input("Enter a colour name: ").lower()
    while colour_choice != "":
        if colour_choice in HEX_COLOURS:
            print("The code for {} is {}".format(colour_choice, HEX_COLOURS[colour_choice]))
        else:
            print("Invalid colour name.")
        colour_choice = input("Enter a colour name: ")

main()