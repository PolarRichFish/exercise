def hello(mesg="hello kitty"):
    if type(mesg) != str:
        raise ValueError("type error: not string")
    print(mesg)

if __name__ == '__main__':
    hello()