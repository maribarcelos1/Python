
def say_what_is(value):
    if value.isalpha():
        print("I'm a letter")
    elif value.isnumeric():
        print("I'm a number")
    else:
        print("Help me, I don't know who I'm")


value = input('digite um valor: ')

say_what_is(value)
