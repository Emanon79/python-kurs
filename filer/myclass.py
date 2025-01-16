class MyClass:
    def print_hello():
        print("Hello from " + __name__)


# Sjekk om vi importeres fra et annet skript, eller kjøres på egen hånd
# __name__ inneholder navnet på modulen koden kjøres fra
if __name__ == '__main__':
    MyClass.print_hello()
