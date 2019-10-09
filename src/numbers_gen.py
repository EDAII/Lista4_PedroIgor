from random import randint
def numbers_gen():
    number_list = []
    while(len(number_list) < 15):
        n = randint(1, 100)
        if not n in number_list:
            number_list.append(n)
    return number_list