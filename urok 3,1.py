try:
    print("start code")
    print(10/0)
    print("no error")
except ImportError:
    print("we have a NAMEerror")
except ZeroDivisionError:
    print("YOU CAN'T DEVIDE BY ZERO")

print("Code after block")