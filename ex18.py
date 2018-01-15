# this one is like your scripts w/ argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this only takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes one
def print_none():
    print("I got nothin'.")

print_two("Misbah","Alam")
print_two_again("Misbah", "Alam")
print_one("Yaga!")
print_none()
