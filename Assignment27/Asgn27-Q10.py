# python script to implemented a nested Try Except block

try:
    print("Outer try block")
    a = int(input('Enter a number for outer try block : '))
    try:
        print('Inner try block')
        b = int(input('Enter a number for inner try block : '))
        print(b)
    except Exception:
        print('Inner exception block')
    finally:
        print('Inner finally block completed')
except Exception:
    print('outer exception block')
finally:
    print('outer finally block completed')