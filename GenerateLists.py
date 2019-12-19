from random import shuffle

def random_list(n):
    A=range(n)
    shuffle(A)
    return A

def copy_list(list):
    copy = []
    for i in range(len(list)):
        copy.append(list[i])
    return copy

