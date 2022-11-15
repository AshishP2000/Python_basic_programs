import logging


def fibo(param1):
    """
    function fibo(): it is printing fibonacci series
    :param param1: int,gives range to for loop
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Fibonacci program")
        a1 = 0
        a2 = 1
        print(a1, a2, end=" ")
        for i in range(2, param1 + 1):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
            print(a3, end=" ")
            logging.info("Finished Fibonacci program")
    except ArithmeticError:
        logging.info(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    x = int(input("Enter range of Fibonacci Series: "))
    fibo(param1=x)
