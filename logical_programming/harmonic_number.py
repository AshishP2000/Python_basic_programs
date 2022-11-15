import logging


def harmonic(input_number):
    """
    function harmonic: calculate and print harmonic value
    :param input_number: int,enter n-th harmonic number
    :return:
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Harmonic Number")
        harms = 1
        for i in range(2, input_number + 1):
            harms += 1 / i
        print(harms)
        logging.info("Finished Harmonic Number")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter N-th Harmonic Number: "))
    harmonic(input_number=number)
