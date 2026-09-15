m = 'I have a secret, i actually would like x to be my boyfriend'
o = 'This message has been deleted'

def send(m):
    with open('Mensaje borrado.txt', 'w') as mens:
        mens.write(m)
        print(f'The message \'{m}\' has been send')

def borrar(n):
    with open('Mensaje Borrado.txt', 'r+') as mens:
        mens.read()
        mens.seek(0)
        mens.truncate(len(n))
        mens.write(n)
        print(f'The message has been erased. Now it will appears like \'{n}\'')


x = input('will you like to send the message?: ')

if x.lower() == 'y':
    send(m)

    y = input('Would you like to erase it?: ')

    if y.lower() == 'y':
        borrar(o)


    else:
        print('The message hasn\'t been erased')

else:
    print('The message has been unsend')




    
    