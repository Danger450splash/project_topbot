# Basics
# OOP then OOP Pillars
# Other Features Type Annotations/Hints & Loop Pattern

from abc import ABC, abstractmethod
import os

class AbstractClass(ABC):

    @abstractmethod
    def user_input(self) -> float:
        pass

class Earth(AbstractClass):

    def __init__(self) -> None:
        os.system('cls')
        self.data = self.user_input()
        os.system('cls')

        print(f'Welcome to Planet Earth, Captain!')
        print(f'Total Human Population: {self.__humans()}')
        print(f'Total Animal Populaton: {self.__animals()}')
        self.__earth_lifespan(self.__miracle(self.data))

    def user_input(self) -> float:
        self.__userdata = float(input("Enter desired lifespan for planet Earth: "))
        return self.__userdata

    def __humans(self) -> int:
        self.__male: int = 4000000000
        self.__female: int = 2000000000
        self.__population: int = (self.__male) + (self.__female)
        return self.__population

    def __animals(self) -> int:
        self.__land: int = 400000
        self.__air: int = 200000
        self.__water: int = 400000
        self.__population: int = (self.__land) + (self.__air) + (self.__water)
        return self.__population

    def __miracle(self, magic: float) -> float:
        self.__respawn: float = magic

        if magic <= 5:
            self.__set_star_to: int = 5
            print(f'Star is set to 5')
        else:
            self.__set_star_to: int = 10
            print(f'Star is set to 10')

        self.__stars = self.__set_star_to
        for rows in range(1, self.__stars+1):
            num = 1
            for columns in range(self.__stars+1, 0, -1):
                if columns > rows:
                    print(" ", end='')
                else:
                    print("*", end=' ')
                    num += 1
            print()

        return self.__respawn

    def __earth_lifespan(self, lifespan: float) -> float:
        self.__category: str = "lifespan"
        self.__earth_mode: list = ["Low", "Medium", "High", "Extreme"]

        if lifespan <= 49.9:
            print(f'The remaining {self.__category} is {lifespan}', self.__earth_mode[0])
        elif lifespan <= 79.9:
            print(f'The remaining {self.__category} is {lifespan}', self.__earth_mode[1])
        elif lifespan <= 100.9:
            print(f'The remaining {self.__category} is {lifespan}', self.__earth_mode[2])
        elif lifespan > 100:
            print(f'The remaining {self.__category} is {lifespan}', self.__earth_mode[3])
