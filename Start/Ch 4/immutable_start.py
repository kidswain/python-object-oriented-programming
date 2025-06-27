# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, new_value: str):
        # this function cannot change any values
        self.value2 = "new_value"  # type: ignore # raises FrozenInstanceError 


obj = ImmutableClass("Another String", 20)
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "New Value"  # raises FrozenInstanceError
# TypeError: cannot assign to field 'value1'

# TODO: even functions within the class can't change anything
obj.some_func("New Value")  # raises FrozenInstanceError
# TypeError: cannot assign to field 'value2'