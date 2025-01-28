# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __eq__(self, other):
        return self.course == other.course

    def __getitem__(self, key):
        if key == 'course':
            return self.course
        else:
            raise Exception(f"Unknown key {key}")

    def __getattr__(self, attr):
        return self.course

# Implementering av methoder som brukes ves spesielle syntax

t1 = Teacher("Joakim", "Python")
t2 = Teacher("Per Erik", "Python")

if t1 == t2:
    print("Teaches the same course")
else:
    print("Teaches different courses")


print(t1["course"])
#print(t1["undef"])

print(t1.lol)
print(t1.undef)
