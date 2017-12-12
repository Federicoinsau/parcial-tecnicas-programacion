def encontrarBotesEnMapa(mapa):

    listaResultado = []

    if mapa != [] and mapa != [""]:
        for fila in mapa:
            if len(fila) == len(mapa[0]):
                if not fila.isspace():
                    letra = 'b'
                    posicion = ([pos for pos, char in enumerate(fila) if char == letra])
                    posicionnueva = posicion
                    listaResultado.append(posicionnueva)

                else:
                    return listaResultado
            else:
                return listaResultado
        return listaResultado
    else:
        return listaResultado

def restoListaDeTuplas(listaDeTuplas):

    listaDeDisparosRestada = []

    for row in listaDeTuplas:
        row = list(row)
        row[0] = row[0] - 1
        row[1] = row[1] - 1
        listaDeDisparosRestada.append(row)
    return listaDeDisparosRestada

def comparoGolpes(listaResultado,listaDeDisparosRestada):
    ele = []
    listaResultado.remove([])

    disparos = listaDeDisparosRestada
    barcos = listaResultado
    for x in barcos:
        for n in disparos:
            if x == n:
                    ele.append(x)
            else:
                continue
def ejercicio2(mapa,listaDeTuplas):
    listaResultado = encontrarBotesEnMapa(mapa)
    listaDeDisparosRestada = restoListaDeTuplas(listaDeTuplas)
    comparoGolpes(listaResultado,listaDeDisparosRestada)


    return

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

#assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])