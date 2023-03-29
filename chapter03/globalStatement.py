# Write your code here :-)
# If you need to modify a global variable from within a function

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
