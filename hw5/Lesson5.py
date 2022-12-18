value = input("Input your value")

for symb in value:
    if symb.isdigit() and int(symb) % 2 == 0:
        print(' This is the even number')
    elif symb.isdigit() and int(symb) % 2 != 0:
        print(' This is the not even number')
    elif symb.islower():
        print(' This is the small letter')
    elif symb.isupper():
        print(' This is the capital letter')
    else:
        print(' This is the a symbol')

        
import time
while True:
    print('I love Python')
    time.sleep(4.2)

