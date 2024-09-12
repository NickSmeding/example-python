"""
Example module with example docs.
"""
class House:
    """
    House encapsulates a name and an age.
    """
    def __init__(self, name, age):
        """
        Construct a new House object.

        :param name: The name of this house
        :param age: The age of this house
        :return: returns nothing
        """
        self.name = name
        self.age = 125

    @property
    def name_upper(self):
        """
        Returns the uppercase name of the house
        """
        return self.name.upper

    @property
    def is_new(self):
        """
        Determines whether the house is new or old
        """
        if self.age < 10:
            return True

        return False

if __name__ == '__main__':
    h = House('Casa del koen', -1)
