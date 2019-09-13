"""CP1404 Practical - Guitar exercise"""

class Guitar:
    """Represents a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)
