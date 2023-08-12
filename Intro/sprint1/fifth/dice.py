import random
from memory import Memory

class Dice:
    '''
    This is the highest superclass of any dice-like object within this project. It shall hold any 
    attributes vital for all dice objects.

    Attributes:
        id (string): an identifier consiting of object type (dice) and its uniquely assigned number.
    '''
    def __init__(self, id: int) -> None:
        self._identifier = "dice_%s" % id

    def throw(self, memory: Memory) -> None:
        '''
        Indicates the throw of a dice-like object that inheirts from this class.

        Arguments:
            memory: a singleton instance of data structure keeping the logs.
        
        Returns:
            int: the result of throw dice indicating faulty inheritence implementation (proper
                    should return any integer >= 1)
        '''
        print("Throwing %s ..." % self._identifier)

class MaxHundredDice(Dice):
    '''
    This is a subclass of Dice supportin up to 100 sides. The throw is meant to run in a thread.

    Attributes:
        id (string): an identifier consiting of object type (dice) and its uniquely assigned number.
        sides (int): randomly chosen number of sides of the dice.
    '''
    def __init__(self, id: int) -> None:
        super().__init__(id)

    def color(self, color):
        self._color = color
        return self

    def sides(self, nr):
        self._sides = random.randint(1, nr)
        return self
        


    def throw(self, memory: Memory) -> None:
        '''
        Extend the functionality of superclass method.
        This method extends the functionality with the throw with respect to the number of sides
        of the dice.

        Arguments:
            memory: a singleton instance of data structure keeping the logs. 

        Returns:
            int: result from the dice throw.

        '''
        super().throw(memory)
        result = random.randint(1, self._sides)
        print("Result from %s: %s" % (self._identifier, result))
        memory.insert_result(result)