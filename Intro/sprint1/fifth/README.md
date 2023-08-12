# Dice rolling engine
This scope of this project is defined as a improved dice rolling service for company X. The improvement involves: 
 - support of 1 to 5 dices simultaniously
 - support of dices with sides from range [1,100]
 - support of multiple throws of all dices
 - extend memory log to keep last 100 throws
 - modularization of code according to OOP

The tech stack requires Python 3.10, Flask library along with mutiple native Python imports (fx. random, threading). 

### Assumptions
 - support of up to 5 dices suggests that their actual count is dictated at random from range [1,5]
 - support of up to 100 sides per dice suggests that sides number id dictated at random from range [1,100]
 - all dices are thrown at once with multithreading concept when request hits the endpoint 
 - scores are written to a singular instance of queue collection as it is suitable for multithreaded read/writes. It keeps max last 100 entries with FIFO concept - new entries added to the rear exceeding the limit will pop the first front entry out. 

### Testing
1. Manual

In order to manually try the enging one should run the `python main.py` locally and submit a request with fx. curl or through Postman to `http://127.0.0.1:8888/throwdice`.

2. Unit testing

Simple unit test are provided in the `/test` folder. They include test of the engine in predictable circumstances as well as stress testing (if memory does not exceed 100). They can be ran with `pytest -q .` when inside the folder. As the engine uses randomized number of dices, a seed is provided for predictability reasons.

### Future, possible improvements
- use array to store scores
- use of dictionary with keys including the id of the dice (better traceability of the service)
- return more indicative response body to `/throwdice` reuqest
- use logging package
- wrap funtions andn methods in try-catch clause
- create custom threadable class

### Changelog
8.07.2023 - creation