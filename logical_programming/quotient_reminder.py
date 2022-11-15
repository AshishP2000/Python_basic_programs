import logging


def quotient_reminder(divident, divisor):
    """
    function quotient_reminder: it takes divident and divisor and prints Quotient and Reminder
    :param divident: int,it is divident
    :param divisor: int,it is divisor
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started quotient_reminder")
        quotient = divident / divisor
        reminder = divident % divisor
        print("Quotient:", quotient)
        print("Reminder:", reminder)
        logging.info("Finished quotient_reminder")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number1 = int(input("Enter Divident: "))
    number2 = int(input("Enter Divisor: "))
    quotient_reminder(divident=number1, divisor=number2)
