"""CP1404 Practical - Programming Language exercise"""

class ProgrammingLanguage:
    """Represents a programming language object"""

    def __init__(self, name="", typing="", reflection, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if language typing is dynamic, false if not"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __repr__(self):
        """String printing"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
