import logging


def prime_anagram_palindrome(input_number):
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started prime_anagram_palindrome")
        list = []
        for i in range(1, input_number + 1):
            flag = 0
            for j in range(1, i + 1):
                if (i % j == 0):
                    flag = flag + 1
            if (flag <= 2):
                list.append(i)
        print(list)
        for i in list:
            reverse = 0
            j = i
            while i != 0:
                num = i % 10
                reverse = (reverse * 10) + num
                i = int(i / 10)
            if (j == reverse):
                print(j, "is Prime and Palindrome")
        logging.info("Finished prime_anagram_palindrome")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Give the range of prime number: "))
    prime_anagram_palindrome(input_number=number)
