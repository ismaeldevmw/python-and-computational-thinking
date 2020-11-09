# def print_message():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones')
#
# print_message()
# print_message()
# print_message()

def conversation(message):
    print('Hola')
    print('Cómo estás')
    print(message)
    print('Adios')

opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    conversation('Elegiste la opción 1')
elif opcion == 2:
    conversation('Elegiste la opción 2')
elif opcion == 3:
    conversation('Elegiste la opción 3')
    conversation('Elegiste la opción 3')
else:
    print('Escribe la opcion correcta')