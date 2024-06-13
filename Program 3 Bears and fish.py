#Program 3 Bears and fish
#                      What does this program do?
#Daniel Jaffe
#                            Date modified: 6/12/24

from abc import ABC, abstractmethod
from random import randint
from random import choice
from random import uniform

#The parent class
class Animal(ABC):
    def __init__(self):
        self._strength = randint(1,5)
        self._is_female = choice([True, False])
        self._death_count = 0

    #Determining which direction the animal will move
    @abstractmethod
    def move(self):
        pass
    #Controling the death count
    @abstractmethod
    def increase_death_count(self):
        pass

    #Overloading the equal siqn for comparing genders
    #Got the equal statement from chatgpt I thought it was 'equ'
    def __eq__(self,other):
        return self._is_female == other._is_female
    #Overloading the greater than so it compares strength property
    def __gt__(self, other):
        return self._strength > other._strength

    #Getters
    def get_strength(self):
        return self._strength

    def get_is_female(self):
        return self._is_female

    def get_death_count(self):
        return self._death_count

    #Setters
    def set_strength(self, strength):
        self._strength = strength

    def set_is_female(self, is_female):
        self._is_female = is_female

    def set_death_count(self, death_count):
        self._death_count = death_count

    #Property
    strength = property(get_strength,set_strength)
    is_female = property(get_is_female,set_is_female)
    death_count = property(get_death_count,set_death_count)

#The bear class is a child class of animal class
class Bear(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        self.direction =  choice([-1,1])


    def increase_death_count(self):
        self._death_count += 1

    #Two bears fight one bear wins and takes up the other space
    def fight(self,other):
        if self._strength > other._strength:
            return "_"

    #Bears mate and new bear is formed
    def mate(self,other):
        return Bear()
    #Bear is eatting the fish
    def eat(self,other):
        return self._strength > other._strength
    #Returns a B for bear
    def __str__(self):
        return "B"

#The fish class is a child class of the animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        self.direction =  choice([-1,1])

    #Fish fight each other but don't change location
    def fight(self,other):
        if self > other:
            other.increase_death_count()
        if other > self:
            self.increase_death_count()

    #Fish make 3 new fish when mating
    def mate(self,other):
        return 3*Fish()

    def increase_death_count(self):
        self._death_count += 1

    #A fish tries to flee from a bear
    def flee(self):
        # Chatgpt showed me how uniform works
        # Uniform allows me to gereate a random floating number
        self.random_flee =  uniform(0.0,1.0)
        #If random number is greater than 0.8 the fish flees successfully
        if self.random_flee > 0.8:
            return True
        else:
            return False

    #returns a F for fish
    def __str__(self):
        return "F"


#Main program
#Initialize the array of 50 animals and array of numbers
array_of_numbers = []
array_of_animals = []

#Creating a array of 50 animals either fish or bear or space
for i in range(1,51):
    array_of_numbers.append(randint(1,10))
print(array_of_numbers)

#Now changing the array of number to actual animal objects
for i in range(0, 50):
    if array_of_numbers[i] == 1:
        array_of_animals.append(Bear())
    elif array_of_numbers[i] == 2 or array_of_numbers[i] == 3 or array_of_numbers[i] == 4 or array_of_numbers[i] == 5:
        array_of_animals.append(Fish())
    else:
        array_of_animals.append("_")
for animal in array_of_animals:
    print(animal, end = "")

# how will the animal move
# for i in range(1,101):
#     if array_of_animals[i] == "_":
#         continue
#     elif array_of_animals[i] == "B":
