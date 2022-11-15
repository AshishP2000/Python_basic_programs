import logging


def vowel_consonant(input_char):
    """
    function vowel_consonant: check if entered character is vowel or consonant
    :param input_char: char,takes input as character
    :return:
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started vowel_consonant")
        input = input_char.lower()
        if (input_char.isdigit()):
            print("Entered number!...")
        else:
            if input == 'a':
                print("It is Vowel")
            elif input == 'e':
                print("It is Vowel")
            elif input == 'i':
                print("It is Vowel")
            elif input == 'o':
                print("It is Vowel")
            elif input == 'u':
                print("It is Vowel")
            else:
                print("It is Consonant")
        logging.info("Finished vowel_consonant")
    except NameError:
        logging.error(NameError)
        print(NameError)


if __name__ == '__main__':
    char = input("Enter character to check Vowel or Consonant: ")
    vowel_consonant(input_char=char)
