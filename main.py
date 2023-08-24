"""Please continue, only if you have a basic understanding of python"""
"""Please keep in mind, most outputs in this will be different for you as they are almost all RANDOM"""
### Imports
import random

### Defining variables
countries = ["North America", "Italy", "France", "England", "Mongolia"]
ages = [1, 7, 55, 23, 91, 14, 19, 50]

### General Function Preview
def random_function_name(args, *kwargs):
  """Module.Function"""
  random_functionName = random.function()
  print(random_functionName)
  """Output: theOutput"""

### Random Functions
def _random():
    """Random.random"""
    random_random = random.random()
    print(random_random)
    """Output: 0.8975066626061244"""

def _randint(start_num: int = 1, end_num:int = 100):
    """random.randint"""
    """Parameters are range for the random integer"""
    random_randint = random.randint(start_num, end_num)
    print(random_randint)
    """Output: 71"""


def _choice():
    """random.choice"""
    random_choice = random.choice(countries)
    print(random_choice)
    """Output: Italy"""


def _shuffle():
    """Random.shuffle"""
    random_shuffle = random.shuffle(ages)
    print(ages)
    """Output: [19, 14, 7, 1, 91, 55, 50, 23]"""

