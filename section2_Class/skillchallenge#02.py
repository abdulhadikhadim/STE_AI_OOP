from string import ascii_letters, punctuation
from random import choices
from copy import copy
 
 
class Password:

 
    INPUT_UNVIERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }
 
    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }
 
   
    def show_input_universe(cls):

        return cls.INPUT_UNVIERSE
 
    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length
 
        self._generate()
 
    def _generate(self):

 
        population = copy(self.INPUT_UNVIERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)
 
        if self.strength == "high":
            population += self.INPUT_UNVIERSE["numbers"] + self.INPUT_UNVIERSE["punctuation"]
        else:
            population += self.INPUT_UNVIERSE["numbers"]
 
        self.password = "".join(list(map(str, choices(population, k=length))))
 
 
if __name__ == "__main__":
    p_weak = Password(strength="low")
    print("Weak password: " + p_weak.password)
 
    p_mid = Password(strength="mid", length=40)
    print("Mid password: " + p_mid.password)
 
    p_high = Password(strength="high")
    print("High password: " + p_high.password)
 
    p_default = Password()
    print("Default password: " + p_default.password)