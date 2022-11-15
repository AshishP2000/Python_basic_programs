import logging


def even_odd(input_number):
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started even_odd")
        if input_number % 2 == 0:
            print(input_number, "is Even")
        else:
            print(input_number, "is Odd")
        logging.info("Finished even_odd")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter number to check Even or Odd: "))
    even_odd(input_number=number)
