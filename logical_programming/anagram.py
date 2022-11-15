import logging


def anagram(input_str1, input_str2):
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started anagram")
        arr1 = list(input_str1.strip())
        arr2 = list(input_str2.strip())
        lis1 = []
        lis2 = []
        l = len(arr1)
        l1 = len(arr2)

        for i in range(0, l):
            for j in range(0, l):
                if arr1[i] < arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
        j = ""
        for i in range(0, l):
            j = j + arr1[i]
        lis1.append(j)

        for i in range(0, l1):
            for j in range(0, l1):
                if arr2[i] < arr2[j]:
                    arr2[i], arr2[j] = arr2[j], arr2[i]
        j = ""
        for i in range(0, l1):
            j = j + arr2[i]
        lis2.append(j)

        if lis1 == lis2:
            print(input_str1, "and", input_str2, "are Anagram")
        else:
            print(input_str1, "and", input_str2, "are not Anagram")
        logging.info("Started anagram")
    except ArithmeticError:
        print(ArithmeticError)
    except Exception:
        print(Exception)


if __name__ == '__main__':
    str1 = input("Enter 1st String: ")
    str2 = input("Enter 2nd String: ")
    anagram(input_str1=str1, input_str2=str2)
