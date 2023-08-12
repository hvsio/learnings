from dice import MaxHundredDice
import random
from flask import Flask
from memory import Memory
from multi_throw import MultiThrow


app = Flask(__name__)

def initialize_globals():
    '''
    One of the main functions starting the engine.
    Initializates shareable data structures.
    '''
    return (memory := Memory(100), dices := [], running_threads := [])

def api_definition(memory, dices, running_threads) -> None:
    '''
    One of the main functions starting the engine.
    Provides definition of API endpoint and the before/after request maintenance tasks.
    '''
    @app.route('/throwdice', methods=['GET'])
    def throw_dice():
        MultiThrow.throw_threaded(dices, memory, running_threads)
        return {'data': ''}, 200

    @app.after_request
    def after_request_func(response):
        print("Memory stack after: %d" % memory.logs.qsize())
        for t in running_threads: t.join()
        running_threads.clear()
        return response

    @app.before_request
    def before_request_func():
        print("Memory stack before: %d" % memory.logs.qsize())


def initialize_dices(dices, fixed_nr = False) -> None:
    '''
    One of the main functions starting the engine.
    Initializates available dices in a fluent interface.
    '''
    dices_count = random.randint(1,5) if not fixed_nr else fixed_nr
    print("Total of %d dices" % dices_count)
    for i in range(dices_count): dices.append(MaxHundredDice(i).color('white').sides(100))


if __name__ == "__main__":
        memory, dices, running_threads = initialize_globals()
        initialize_dices(dices)
        api_definition(memory, dices, running_threads)
        app.run(port=8888)
    

