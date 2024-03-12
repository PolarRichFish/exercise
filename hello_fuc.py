
def build_message(user="kitty", mode='cap'):
    if mode == 'cap':
        message = "Hello " + user
    else:
        message = "HELLO " + user
    return message

def over_p():
    print("it is done")

def hello(mesg="hello kitty"):
    if type(mesg) != str:
        raise ValueError("type error: not string")
    print(mesg)
    over_p()

if __name__ == '__main__':
    hello(build_message())