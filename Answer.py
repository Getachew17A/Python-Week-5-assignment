# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # Encapsulated attribute

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        return f"{self.name} leveled up to {self.__level}!"

# Subclass with polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def introduce(self):  # Polymorphic override
        return f"{self.name} soars through the sky at {self.flight_speed} km/h with {self.power}!"

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, level, gadgets):
        super().__init__(name, power, level)
        self.gadgets = gadgets

    def introduce(self):  # Another polymorphic override
        return f"{self.name} uses {', '.join(self.gadgets)} to unleash {self.power}!"

superman = FlyingHero("superman", "Wind Slash", 5, 300)
cyber = TechHero("Cyber", "shooting guns", 7, ["Drone", "bomber"])

print(superman.introduce())
print(cyber.introduce())
print(superman.level_up())
print(cyber.get_level())
