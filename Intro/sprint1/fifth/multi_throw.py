from threading import Thread

class MultiThrow:
    '''
    Class holding generic (hence static) methods for throwing dices in a multithreading manner.
    '''
    def __init__(self):
        pass

    @staticmethod
    def throw_threaded(dices, memory, running_threads):
        '''
        Static method executing simultanous throws of available dices.

        Arguments:
            dices: list - list of dice-like objects
            memory: Memory - object holding the logs as a queue
            running_threads - list with all active threads
        '''
        print("Dice throwing!")
        for d in dices:
            thread = Thread(target=d.throw, args=(memory,))
            thread.start()
            running_threads.append(thread)