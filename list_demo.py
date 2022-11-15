
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25]  # Initializing list
    print("Lis of Squares:", squares)  # print list

    print("Index 0:", squares[0])  # indexing returns item
    print("last element:", squares[-1])  # last element
    print(squares[-3:])  # slicing returns new list
    print(squares[:])

    print(squares + [36, 49, 64, 81, 100])

    colors = ['red', 'green', 'blue']
    print(colors)

    # Adding elements to list
    numbers = [1, 2, 3, 4]
    numbers.append(5)  # add element in the end
    print(numbers)
    numbers.insert(1, 6)  # add element at specific index
    print(numbers)
    del numbers[1]  # del element using index
    print(numbers)
    numbers.pop()  # remove element from last
    print(numbers)
    numbers.pop(1)  # remove element at specific index using pop
    print(numbers)
    numbers.remove(3)  # remove given element
    print(numbers)

