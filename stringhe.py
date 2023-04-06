#stringhe come array

x = "provaDiStringa"
y = 'ciao'

print(x)
print(y)

print(x[0])
print(len(x))

# ciclo for
for carattere in "computer":
    print(carattere)

#parti di stringa, primi tre caratteri
print(x[:3])

print(x[2:7])

# modifiche di stringhe
print(x.upper())
print(x.lower())

x1 = " ciao ciccio carmine "
print(x1.strip())

print(x1.replace("c", "W"))