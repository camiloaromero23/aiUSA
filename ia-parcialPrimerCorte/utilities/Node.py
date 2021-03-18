class Node:

    def __init__(self, name="", fathers=[]):
        self.name = name

    def __eq__(self, otherNode):
        return self.name == otherNode.name

    def __str__(self):

        return self.name

    def __repr__(self):
        return self.__str__()
