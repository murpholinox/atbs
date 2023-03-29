# Write your code here :-)

def spam():
    global eggs # global
    eggs = 'spam'

def bacon():
    eggs = 'bacon' # local

def ham():
    print(eggs) # toma la global

eggs = 42
spam()
print(eggs)
