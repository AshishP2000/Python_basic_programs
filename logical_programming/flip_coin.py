import logging
import random


def flip_coin(input_number):
    """
    function reverse_number: to flip a coin
    :param input_number: int,taking only input from user
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Flip coin: ")
        n = 0
        count1 = 0
        count2 = 0
        for i in range(0, input_number):
            r = random.randint(0, 1)
            if r < 0.5:
                count1 += 1
            else:
                count2 += 1
        perH = (count1 * 100) / input_number
        perT = (count2 * 100) / input_number
        print("Percentage of Heads:", perH)
        print("Percentage of Tails:", perT)
        logging.info("Finished Flip coin")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter how many times coin will flip: "))

    flip_coin(input_number=number)
