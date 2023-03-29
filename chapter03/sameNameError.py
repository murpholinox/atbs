# Write your code here :-)
def spam():

    print(eggs) # Error
    eggs = 'spam local'
    # está extraño si comentamos la línea superior, spam imprime huevos que es global.
    # pero si definimos la variable localmente, da error.
    # si se hace la asignación de la variable antes de usarla, no hay tal error.
eggs = 'global'
spam()
