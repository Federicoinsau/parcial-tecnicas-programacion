def reciboMapaYListaDeTuplas(mapa, listaDeTuplas):

    listaResultado = []

    if mapa != [] and mapa != [""]:
        for fila in mapa:
            if len(fila) == len(mapa[0]):
                if not fila.isspace():
                    for posicion in fila:
                        if posicion == 'b' or posicion == '.':
                            if posicion == 'b':
                                posicion = fila.index('b')
                                posicionnueva = posicion
                                listaResultado.append(posicionnueva)
                        else:
                            return listaResultado
                else:
                    return listaResultado
            else:
                return listaResultado
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