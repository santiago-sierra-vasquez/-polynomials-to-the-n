from ntpath import join
from itertools import product
import sys
sys.setrecursionlimit(10000)


# Esta lista es importante ya que con el numero de "cantidad de letras" que nos da el usuario sabremos con las letras que trabajaremos


lista_de_cantiadad_de_letras = {
    1 : "a",
    2 : ["a", "b"],
    3 : ["a", "b", "c"],
    4 : ["a", "b", "c", "d"],
    5 : ["a", "b", "c", "d", "e"],
    6 : ["a", "b", "c", "d", "e", "f"],
    7 : ["a", "b", "c", "d", "e", "f", "g"],
    8 : ["a", "b", "c", "d", "e", "f", "g", "h"],
    9 : ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
    10 : ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
}



# Esta funcion le pide los datos al usuario y devuelve 3 datos importantes

def setup():
    cantidad_de_letras = int(input("¿Cantidad de letras? "))
    letras = lista_de_cantiadad_de_letras[cantidad_de_letras]
    exponente = int(input("Exponente: "))
    numero = "a"
    for list_number in range(1, len(letras)):
        numero += f" + {letras[list_number]}"

    if input(f"({numero})^{exponente}?, Y/N ").lower() == "n":
        setup()
    else:
        return[exponente, letras, cantidad_de_letras]


# Esta funcion usando el exponente y las letras, hace la combianatoria de esta, pero me lo entrega en una lista que dentro tiene tuplas
# Asi que con un for loop saco los valores de las tuplas


def convert():
    list2 = []
    for number in range(0, exponente):
        list2.append(letras)
    the_print = list((product(*list2)))
    the_new_print = []

    for i in range(0, len(the_print)):
        the_new_print.append("".join(the_print[i]))

    return the_new_print


#  Con esta funcion el rpograma detecta si dentro de un elemento de la lista hay letras repetidas, si las hay las simplifica a una potenciacion
# Este programa es muy utili por que en cierta manera organiza la lista, es decir primera pone las a luego las b y asi, es decir la lista queda
# Organizada para la siguiente fase


def simplification(letras):
    times_for_letter = 0
    simplify_expresion_for_letters = ""
    position = 0
    simplicacion_n_1 = []
    for number in range(0,  cantidad_de_letras ** exponente):
        for letter in letras:
            if the_print[position].count(letter) != 0:
                if the_print[position].count(letter) == 1:
                    if times_for_letter == 0:
                        simplify_expresion_for_letters += (f"{letter}")
                        times_for_letter += 1
                    else:
                        simplify_expresion_for_letters += (f" * {letter}")
                        times_for_letter += 1
                else:
                    if times_for_letter == 0:
                        simplify_expresion_for_letters += (f"{letter}^{the_print[position].count(letter)}")
                        times_for_letter += 1
                    else:
                        simplify_expresion_for_letters += (f" * {letter}^{the_print[position].count(letter)}")
                        times_for_letter += 1

 
        simplicacion_n_1.append(simplify_expresion_for_letters)        
        position += 1
        times_for_letter = 0
        simplify_expresion_for_letters = ""


    return simplicacion_n_1


# Esta funcion detecta si hay elementos repetidos en la lista, y si los hay los simplifica con una multiplicacion


def find_repeat(the_list):
    repeated_numbers = []
    seen = set()
    for num in the_list:
        if num in seen:
            if not num in repeated_numbers:
                repeated_numbers.append(num)
        seen.add(num)


    for number in range(0, len(repeated_numbers)):
        times = the_list.count(repeated_numbers[number])
        value_to_remove = repeated_numbers[number]
        the_list = [value for value in the_list if value != value_to_remove]
        the_list.append(f"{times} * {repeated_numbers[number]}")
    
    return the_list


# Y por ultimo esta funcion convierte la lista, en un string mas leible para el usuario


def organize():
    times = 1
    the_final_result = ""
    for number in the_print:
        if times == 1:
            the_final_result += f"({number})"
        else:
            the_final_result += f" + ({number})"

        times += 1

    return the_final_result


# Invoco al "setup()" y declaro todas la variables que voy a usar

output = setup()
exponente = output[0]
letras = output[1]
posicion = exponente - 1
cantidad_de_letras = output[2]
last_letter = letras[len(letras) - 1]
the_print = []
for letter in range(0, exponente):
    the_print.append("a")


# Realizo la combinatoria

the_print = convert()


# luego empiezo a simplificar


the_print = simplification(letras)

the_print = find_repeat(the_print)


# Y por ultimo esta funcion organiza el resultado de la lista, para luego ser imprimido

the_print = organize()
print(the_print)