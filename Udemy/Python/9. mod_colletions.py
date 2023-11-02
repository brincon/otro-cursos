from collections import Counter
from collections import defaultdict
from collections import namedtuple

# numeros = [8,6,7,7,7,7,8,8,9,9,2,3,4]
# print(Counter(numeros))

# print(Counter("mississippi"))

# frase = "al pan pan y al vino vino"

# print(Counter(frase.split()))

# serie = Counter([7,7,7,7,7,7,8,8,9,9,2,2,2,3,4])
# print(serie.most_common(2))


# mi_dict = {"uno": "verde", "dos": "azul", "tres":"rojo"}
# print(mi_dict["cuatro"])

# mi_dict = defaultdict(lambda: "nada")
# mi_dict["uno"] = "verde"
# print(mi_dict["uno"])
# print(mi_dict["dos"])
# print(mi_dict)


mi_tupla = (500,18,65)
print(mi_tupla[1])

Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
ariel = Persona("ariel", 1.76, 79)

print(ariel.altura)
print(ariel[2])