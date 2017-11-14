def reciboMapaYListaDeTuplas(mapa, listaDeTuplas):
    listaDeBotes = []
    listaResultado = []
    if mapa:
        for fila in mapa:
            for posicion in fila:
                posicion = list(posicion)
                if posicion == ["b"]:
                    posicion = posicion.index("b")
                    listaDeBotes.append(posicion)

    for row in listaDeTuplas:
        row = list(row)
        row[0] = row[0] - 1
        row[1] = row[1] - 1
        listaResultado.append(row)




    else:
        return listaResultado





def ejercicio2(mapa,listaDeTuplas):
    return reciboMapaYListaDeTuplas(mapa, listaDeTuplas)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

#assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])
