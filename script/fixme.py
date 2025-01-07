# Kopier denne koden inn i fixme.py
import json, time

class Person:
    def __init__ (self, name, age):
        self._name =name
        self._age  = age

    
    def say_hello(self):
        greetin = f"Hello my name is {self._name} and I am {self._age} years old"
        print (greeting)

def main():
    me = Person("Joakim", 29)
    you = Person("Student", 20)

    me.say_hello ()
    you.say_hello()


if __name__ == "__main__":
    main()
