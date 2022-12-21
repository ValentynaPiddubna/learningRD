text = input('Enter your text:')
print(text)
if text.isdigit() and int(text) % 2 == 0:
    print('The value is an even number')
elif text.isdigit() and int(text) % 2 != 0:
    print('The value is not even number')
else:
    print(f' You have entered a string value with a length {len(text)} characters')





