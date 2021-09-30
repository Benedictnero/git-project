import random

def gen_num():
    num = int(input('Enter your number:  '))
    for x in range(1,100):
         random_x = random.randint(0,100)
         result = x + num + random_x
    print(f'>>>> {result} <<<<')

gen_num()
