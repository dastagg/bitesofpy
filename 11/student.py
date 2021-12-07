from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _is_valid_operand(self, other):
        return hasattr(other, "name") and hasattr(other, "age")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.age < other.age


student1 = Student("xyz", 23)
student2 = Student("abc", 25)
student3 = Student("lmn", 23)


# print(student1 == student2)
# print(student1 > student2)
# print(student1 < student2)
print(student1 == student3)
print(student1 < student3)
print(student1 <= student3)
print(student1 >= student3)
print(student1 > student3)
print(student1.age == student3.age)
print(student1.name != student3.name)
