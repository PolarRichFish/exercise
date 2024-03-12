
def build_message(user="kitty", mode='cap'):
    if mode == 'cap':
        message = "Hello " + user
    else:
        message = "HELLO " + user
    return message

def hello(mesg="hello kitty"):
    if type(mesg) != str:
        raise ValueError("type error: not string")
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    print(mesg)

if __name__ == '__main__':
    hello(build_message())