import logging


def prime_factorization(input_number):
    """
    function prime_factorization: get the number find factors and after that store it in the list
    and find prime factors of numbers which are stored in the list
    :param input_number: int,for the range of loop
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Prime Factorization")
        list = []
        for i in range(1, input_number + 1):
            if (input_number % i == 0):
                list.append(i)
        n = len(list)
        for i in range(0, n):
            count = 0
            for j in range(1, list[i] + 1):
                if (list[i] % j == 0):
                    count += 1
            if (count == 2):
                print(list[i])
        logging.info("Finished Prime Factorization")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter number to find Prime Factors: "))
    prime_factorization(input_number=number)
