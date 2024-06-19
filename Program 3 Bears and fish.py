# Program 3 Bears and fish
# This program runs a simulation between bears and fish in a ecosystem. We look at different scenarios like eating mating and fighting and how it effects the ecosystem.
# Daniel Jaffe
#                            Date modified: 6/19/24

from abc import ABC, abstractmethod
from random import randint
from random import choice
from random import uniform


# The parent class
class Animal(ABC):
    def __init__(self):
        self._strength = randint(1, 5)
        self._is_female = choice([True, False])
        self._death_count = 0

    # Determining which direction the animal will move
    @abstractmethod
    def move(self):
        pass

    # Controling the death count
    @abstractmethod
    def increase_death_count(self):
        pass

    # Getters
    def get_strength(self):
        return self._strength

    def get_is_female(self):
        return self._is_female

    def get_death_count(self):
        return self._death_count

    # Setters
    def set_strength(self, strength):
        self._strength = strength

    def set_is_female(self, is_female):
        self._is_female = is_female

    def set_death_count(self, death_count):
        self._death_count = death_count

    # Overloading the equal sign for comparing genders
    def __eq__(self, other):
        # Used chatgpt for isinstance
        # isinstance check if a object belongs to a class
        if isinstance(other, Animal):
            return self._is_female == other._is_female

    # Overloading the greater than so it compares strength property
    def __gt__(self, other):
        return self._strength > other._strength

    # Property
    strength = property(get_strength, set_strength)
    is_female = property(get_is_female, set_is_female)
    death_count = property(get_death_count, set_death_count)


# The bear class is a child class of animal class
class Bear(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        return choice([-1, 1])

    def increase_death_count(self):
        self._death_count += 1

    # Checks if the animal reached a death count above 5 if then return a empty spot to replace them
    def Check_death(self):
        if self._death_count > 5:
            return "_"
        else:
            return self
    # Two bears fight one bear wins and takes up the other space
    def fight(self, other):
        if self._strength > other._strength:
            return "B"
        if other._strength > self._strength:
            return "_"

    # Bears mate and new bear is formed
    def mate(self, other):
        # No mating is happening
        if self._is_female == other._is_female:
            return False
        # Mating is happening
        if self._is_female != other._is_female:
            return Bear()

    def eat(self, other):
        # Fish succeeds to flee bears does not eat
        if other == True:
            self._death_count += 1
            # Checks death if death count reaches above 5
            return False
        if other == False:
            self._death_count = 0
            return True

    # Returns a B for bear
    def __str__(self):
        return "B"


# The fish class is a child class of the animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        return choice([-1, 1])

    # Fish fight each other but don't change location
    def fight(self, other):
        if self > other:
            other.increase_death_count()
            # Checks death if death count reaches above 5
        if other > self:
            self.increase_death_count()
            # Checks death if death count reaches above 5

    # Fish make 3 new fish when mating
    def mate(self, other):
        # No mating is happening
        if self._is_female == other._is_female:
            return False
        # Mating is happening
        if self._is_female != other._is_female:
            return [Fish(), Fish(), Fish()]

    def increase_death_count(self):
        self._death_count += 1

    # Checks if the animal reached a death count above 5 if then return a empty spot to replace them
    def Check_death(self):
        if self._death_count > 5:
            return "_"
        else:
            return self

    # A fish tries to flee from a bear
    def flee(self):
        # Chatgpt showed me how uniform works
        # Uniform allows me to gereate a random floating number
        self.random_flee = uniform(0.0, 1.0)
        # If random number is greater than 0.8 the fish flees successfully
        if self.random_flee > 0.8:
            return True
        else:
            return False

    # returns a F for fish
    def __str__(self):
        return "F"


# Main program
# Initialize the array of 50 animals and array of numbers
array_of_numbers = []
orginal_array_of_animals = []

# Creating a array of 50 animals either fish or bear or space
for i in range(0, 50):
    array_of_numbers.append(randint(1, 10))

# Now changing the array of number to actual animal objects
for i in range(0, 50):
    if array_of_numbers[i] == 1:
        orginal_array_of_animals.append(Bear())
    elif array_of_numbers[i] == 2 or array_of_numbers[i] == 3 or array_of_numbers[i] == 4 or array_of_numbers[i] == 5:
        orginal_array_of_animals.append(Fish())
    else:
        orginal_array_of_animals.append("_")

array_of_animals = orginal_array_of_animals
# doing a simulation that if going 100 times
for k in range(0,100):
    # how will the animal move
    i = 0
    while i < 50:
        if array_of_animals[i] == "_":
            i += 1
            continue
        if str(array_of_animals[i]) == "B":
            # Bear moves backward
            bear_movement = array_of_animals[i].move()
            if bear_movement == -1 and i > 0:
                if array_of_animals[i - 1] == "_":
                    # The bear move backward
                    array_of_animals[i - 1], array_of_animals[i] = array_of_animals[i], "_"

                elif array_of_animals[i - 1] == "B":
                    # Bear mates with animal if they are not the same sex
                    childBear = array_of_animals[i].mate(array_of_animals[i - 1])
                    if childBear == type(Bear):
                        # place child bear in an empty spot
                        # This find all the empty spots and put them into a array
                        newIndexSpots = []
                        for i in range(0, 50):
                            if array_of_animals[i] == "_":
                                newIndexSpots.append(i)
                        newIndex = choice(newIndexSpots)
                        array_of_animals[newIndex] = childBear

                    # Bear fight with animal is they are the same sex
                    else:
                        array_of_animals[i].fight(array_of_animals[i - 1])

                elif str(array_of_animals[i - 1]) == "F":
                    if array_of_animals[i].eat(array_of_animals[i - 1].flee()) == True:
                        # Bear eats fish and takes it spot
                        array_of_animals[i - 1] = array_of_animals[i]
                        array_of_animals[i] = "_"
                i += 1
            # Bear moves foward
            elif bear_movement == 1 and i < 49:
                if array_of_animals[i + 1] == "_":
                    # The bear move foward
                    array_of_animals[i + 1], array_of_animals[i] = array_of_animals[i], "_"
                elif str(array_of_animals[i + 1]) == "B":
                    # Bear mates with animal if they are not the same sex
                    childBear = array_of_animals[i].mate(array_of_animals[i + 1])
                    # Checks if childbear is true
                    if childBear == type(Bear):
                        # place child bear in an empty spot
                        # This find all the empty spots and put them into a array
                        newIndexSpots = []
                        for i in range(0, 50):
                            if array_of_animals[i] == "_":
                                newIndexSpots.append(i)
                        newIndex = choice(newIndexSpots)
                        array_of_animals[newIndex] = childBear
                    else:
                        # Bear fight with animal is they are the same sex
                        array_of_animals[i].fight(array_of_animals[i + 1])
                elif str(array_of_animals[i + 1]) == "F":
                    if array_of_animals[i].eat(array_of_animals[i + 1].flee()) == True:
                        # Bear eats fish and takes it spot
                        array_of_animals[i + 1], array_of_animals[i] = array_of_animals[i], "_"
                i += 2
        elif str(array_of_animals[i]) == "F":
            # Fish moves backward
            fish_movement = array_of_animals[i].move()
            if fish_movement == -1 and i > 0:
                if array_of_animals[i - 1] == "_":
                    # The fish  move backward
                    array_of_animals[i - 1], array_of_animals[i] = array_of_animals[i], "_"
                elif str(array_of_animals[i - 1]) == "B":
                    # Fish fails to flee from bear
                    if array_of_animals[i].flee() == False:
                        # Bear takes fishes location
                        array_of_animals[i], array_of_animals[i - 1] = array_of_animals[i - 1], "_"
                elif str(array_of_animals[i - 1]) == "F":
                    # fishes fights with each other
                    childfish = array_of_animals[i - 1].mate(array_of_animals[i])
                    # Checks if child fish is true
                    if childfish == False:
                        # Fish fights itself
                        array_of_animals[i].fight(array_of_animals[i - 1])
                    else:
                        # place child fish in an empty spot
                        # This find all the empty spots and put them into an array
                        j = 0
                        # This gets all three of the fish objects that were made from mating and puts them in a random spot
                        while j < 3:
                            newIndexSpots = []
                            for i in range(0, 50):
                                if array_of_animals[i] == "_":
                                    newIndexSpots.append(i)
                            if len(newIndexSpots) < 3:
                                j += 1
                                continue
                            else:
                                newIndex = choice(newIndexSpots)
                                array_of_animals[newIndex] = childfish[j]
                                j += 1
                            j += 1
                i += 1

            # fish moves foward
            elif fish_movement == 1 and i < 49:
                if array_of_animals[i + 1] == "_":
                    # The fish move foward
                    array_of_animals[i + 1], array_of_animals[i] = array_of_animals[i], "_"
                elif str(array_of_animals[i + 1]) == "B":
                    # Fish fails to flee from bear
                    if array_of_animals[i].flee() == False:
                        # Bear takes fishes location
                        array_of_animals[i], array_of_animals[i + 1] = array_of_animals[i - 1], "_"
                elif str(array_of_animals[i + 1]) == "F":
                    # fishes fights with each other
                    childfish = array_of_animals[i + 1].mate(array_of_animals[i])
                    # Checks if child fish is true
                    if childfish == False:
                        array_of_animals[i].fight(array_of_animals[i + 1])
                    else:
                        # place child fish in an empty spot
                        # This find all the empty spots and put them into an array
                        j = 0
                        # This gets all three of the fish objects that were made from mating and puts them in a random spot
                        while j < 3:
                            newIndexSpots = []
                            for i in range(0, 50):
                                if array_of_animals[i] == "_":
                                    newIndexSpots.append(i)
                            if len(newIndexSpots) < 3:
                                j += 1
                                continue
                            else:
                                newIndex = choice(newIndexSpots)
                                array_of_animals[newIndex] = childfish[j]
                                j += 1
                    # fishes fights with each other
                i += 2
    #Checks the array to make sure no animal has a death count above 5 if so it replaces with empty space
    for n in range(0, 50):
        if str(array_of_animals[n]) == "B" or str(array_of_animals[n]) == "F":
            array_of_animals[n] = array_of_animals[n].Check_death()
    # Prints out the different answer for each results for the simulation
    for animal in array_of_animals:
        print(animal, end="")
    print()
