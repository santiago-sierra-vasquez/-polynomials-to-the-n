from ntpath import join
from itertools import product
import sys
sys.setrecursionlimit(10000)


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

letra_a_numero = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10
}

numero_a_letra = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j"
}



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
        exponente_total = exponente
        return[exponente, letras, cantidad_de_letras]


# Declaro todas la variables

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


list2 = []
for number in range(0, exponente):
    list2.append(letras)

the_print = list((product(*list2)))


def convert():
    the_new_print = []
    for i in range(0, len(the_print)):
        the_new_print.append("".join(the_print[i]))

    return the_new_print


the_print = convert()


# luego empiezo a simplificar
# Estas lineas decodigo detectar si hay multiples letras en cada posicion de la lista y las simplifica


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



simplificacion_n_1 = simplification(letras)


# Esta es la segunda fase de simplificacion en la cual se revisa si en la lista hay repetidos y si los hay simplificarlos para luego imprimit el resultado

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

simplificacion_n_2 = find_repeat(simplificacion_n_1)

# Y por ultimo esta funcion organiza el resultado de la lista, para luego ser imprimido

def organize():
    times = 1
    the_final_result = ""
    for number in simplificacion_n_2:
        if times == 1:
            the_final_result += f"({number})"
        else:
            the_final_result += f" + ({number})"

        times += 1

    return the_final_result

print(organize())