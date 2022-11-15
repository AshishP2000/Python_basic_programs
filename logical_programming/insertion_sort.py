import logging


def insertion_sort(lista):
    """
    param lista: list of string to be sorted
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started insertion sort")
        for i in range(1, len(lista)):
            save = lista[i]
            j = i
            while j > 0 and lista[j - 1] > save:
                lista[j] = lista[j - 1];
                j -= 1
            lista[j] = save
            # optionally show sort progress
            print(lista)
        logging.info("Finished insertion sort")
    except TypeError:
        logging.error(TypeError)
        print(TypeError)


if __name__ == '__main__':
    lista = []
    print("Enter 4 words to be sorted:")
    for i in range(0, 4):
        i = input()
        lista.append(i)
    insertion_sort(lista)
