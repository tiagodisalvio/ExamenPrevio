list1 = [(42727210, "Tiago"), (30846, "Andres"), (82148989,"Rosa")]
list2 = [(5893257, "Tiago"), (65566, "Raul"), (82148989, "Rosa")]
coincidencias = []
for n1 in list1:
    for n2 in list2:
        if n1 == n2 and n1 not in coincidencias:
            coincidencias.append(n1)
repetidos_list2 = []
for n1 in list1:
    for n2 in list2:
        if n2[1] == n1[1]:
            repetidos_list2.append(n2) 
            repetidos_list2.append(n1)

print("Coincidencias:", coincidencias)
print("Presentes:", list1, "Faltantes:", list2)
print("Presentes:", list2, "Faltantes:", list1)
print("Elementos en conflicto:",repetidos_list2)