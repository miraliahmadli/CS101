import random


def drawing_integers(lb, ub, trials):
    """
    Make a list of the integers
    :param lb: the lower bound of the integers
    :param ub: the upper bound of the integers
    :param trials: the number of trials
    :return: an integers list. Ex) [1, 4, 3, 5, 2]
    """
    lst = []
    for i in range(trials):
        lst.append(random.randint(lb, ub))
    return lst


def average_integers(num_list):
    """
    Compute the average of the integers in the num_list
    :param num_list: input list
    :return: average value of the list
    """
    n = len(num_list)
    return sum(num_list) / n


def count_integers(num_list):
    """
    Count the integers in the num_list
    :param num_list: input list
    :return: A list of tuples that consist of the integer and its frequency
    """
    freq = dict()
    for num in num_list:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return list((k, v) for k, v in freq.items())


# Run the program
list1 = drawing_integers(1, 6, 20)
print(list1)
print(average_integers(list1))
print(count_integers(list1))
print()
list2 = drawing_integers(5, 12, 15)
print(list2)
print(average_integers(list2))
print(count_integers(list2))
