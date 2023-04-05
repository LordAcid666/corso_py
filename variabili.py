# Esercizi variabili, tipi e casting

# https://codegrind.it/python/esercizi-variabili/


numero = 5
print(numero)

nome = "Mario"
print(nome)

pi = 3.14
print(pi)

vero_o_falso = True
print(vero_o_falso)

numero_come_stringa = str(numero) # "5"
print(numero_come_stringa)

pi_come_intero = int(pi)
print(pi_come_intero)

vero_o_falso_come_stringa = str(vero_o_falso)
print(vero_o_falso_come_stringa)

x = 10
y = 20
print(x + y)

#9
z = "30"
#z = int(z)
print(x + y + int(z))

#10
stringa_1 = "hello"
stringa_2 = "world"
stringa_concatenata = stringa_1 + " " + stringa_2
print(stringa_concatenata)

#11
variabile_bool = True
# if type(variabile_bool) == bool:
#     print(variabile_bool)
print(type(variabile_bool) == bool)

#12
lista = [1, 2, 3]
print(type(lista) == list)