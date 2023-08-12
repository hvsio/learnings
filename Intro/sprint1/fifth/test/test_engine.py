import pytest
from multi_throw import MultiThrow
import random
from engine import initialize_dices, initialize_globals
import time

class TestEngine():
    random.seed(0)

    def test_regular_throws(self):
        memory, dices, running_threads = initialize_globals()
        initialize_dices(dices)
        MultiThrow.throw_threaded(dices, memory, running_threads)
        time.sleep(2)
        assert memory.logs.qsize() == 4

    def test_stress_memory(self):
        memory, dices, running_threads = initialize_globals()
        initialize_dices(dices, 25)
        for _ in range(10): MultiThrow.throw_threaded(dices, memory, running_threads)
        time.sleep(2)
        assert memory.logs.qsize() == 100



