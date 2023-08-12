from queue import Queue

class Memory:
    '''
    A class holding memory logs with its specific properties and functions.

    Attributes:
        size (int): maximum number of past logs to keep.
        logs (Queue): a data structure keeping the logs with FIFO concept. Safe for multithreaded read/writes
                    coming from dice-like objects.
    '''

    def __init__(self, size: int) -> None:
        self.logs = Queue(maxsize=size)

    def insert_result(self, result: int) -> None:
        '''
        This method inserts new result provided the check for capacity indicates available space.
        Otherwise pop the result from the front (the oldest).

        Arguments:
            result (int): result of a dice-like object to be inserted as a log.
        '''
        if self.logs.full():
            self.logs.get()
        self.logs.put(result)