import random
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'제 이름은 {self.name}입니다')

class Teacher(Person):
    # No required declarations of variables

    
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def greet(sel):
        print(f"Hi, my name is {sel.name} and I teach {sel.course}")

    #@decorator // Implicit self or not?
    def select_new_course(self, courses):
        # Local variable or instance attribute? No declaration
        course = courses[random.randrange(0, len(courses))]

    """
    Proposal
    def self.greet():
        pass
    """

t = Teacher("Joakim", "Python")

# These are equivalent
Teacher.greet(t)
t.greet()

# Calling parent class overridden method
Person.greet(t)

t.select_new_course(['Java', 'C++', 'Haskel'])
t.greet()
