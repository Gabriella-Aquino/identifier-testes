import sys
from identifier import Identifier

def main():
    if len(sys.argv) == 1:
        print("Uso: python identifier_main.py <string>")
    else:
        id_checker = Identifier()
        input_str = sys.argv[1]

        if id_checker.validate_identifier(input_str):
            print("Valido")
        else:
            print("Invalido")

if __name__ == "__main__":
    main()
