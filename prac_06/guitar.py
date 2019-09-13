"""CP1404 Practical - Guitar exercise"""

class Guitar:
    """Represents a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2019 - self.year
        return age

    def is_vintage(self):
        vintage = get_age()
        if vintage > 50:
            return True
        else:
            return False

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)
