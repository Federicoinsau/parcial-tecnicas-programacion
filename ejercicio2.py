def reciboMapaYListaDeTuplas(mapa, listaDeTuplas):
    listaResultado = []
    for fila in mapa:
        for posicion in fila:
            if posicion == "b":
                indice = (fila.index(posicion), posicion.index(""))
                listaResultado.append(indice)
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
