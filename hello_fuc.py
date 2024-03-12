
def build_message(user="kitty"):
    message = "HELLO " + user
    return message

def over_p():
    print("it is done")

def hello(mesg="hello kitty"):
    if type(mesg) != str:
        raise ValueError("type error: not string")
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    print(mesg)
    over_p()

if __name__ == '__main__':
    hello(build_message())