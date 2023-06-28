def divide():
    print('Enter your dividend:')
    dividend = int(input())
    print('Enter your divisor:')
    divisor = int(input())
    quotient = dividend // divisor
    remainder = dividend % divisor
    print('{} / {} = {} ...... {}'.format(dividend, divisor, quotient, remainder))

def mutiple():
    print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("divide or mulitiply:")
    op = input()
    if op == 'divide':
        divide()
    else:
        mutiple()
