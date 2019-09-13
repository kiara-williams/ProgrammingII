"""CP1404 Practical - Programming Language exercise"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    language_list = [ruby, python, visual_basic]
    print(language_list)

    dynamic_languages = []

    for language in language_list:
        if language.is_dynamic():
            dynamic_languages.append(language.name)

    print("The dynamically typed languages are:")
    for language_name in dynamic_languages:
        print(language_name)

main()