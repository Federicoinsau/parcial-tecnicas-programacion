def rotaciones(palabra):

    listaderotaciones = []

    for i in palabra:
        if i == palabra[:1] and not palabra.isspace():
            listaderotaciones.append(palabra)
            if (len(palabra) > 1):
                for letra in palabra:
                    if letra != palabra[:1]:
                        palabra = palabra[1:] + palabra[:1]
                        listaderotaciones.append(palabra)

            return listaderotaciones

        else:
            return listaderotaciones


    return listaderotaciones


def ejercicio1(palabra):
    return rotaciones(palabra)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])