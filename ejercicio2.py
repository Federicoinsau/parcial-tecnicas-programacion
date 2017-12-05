def posicionesDeBarcos(mapa):

    mapaBase = []

    if mapa != [] and mapa != [""] and len(mapa) > 1:
        for fila in mapa:
            if not fila.isspace() and len(fila) == len(mapa[1]):
                for n in range(len(mapa)):
                    for m in range(len(mapa)):
                        for i in mapa:
                            for j in i:
                                if j == "b":
                                    mapaIngresado = (n, m)
                                    mapaBase.append(mapaIngresado)
                    return mapaBase
            else:
                return mapaBase
    else:
        return mapaBase

def restarNumeroDeIndice(listaDeTuplas):

    listaDeDisparosRestada = []

    for row in listaDeTuplas:
        row = list(row)
        row[0] = row[0] - 1
        row[1] = row[1] - 1
        listaDeDisparosRestada.append(row)
    return listaDeDisparosRestada


def sumarNumeroDeIndice(listaDeDisparosRestada):

    listaSobrevivientesSumada = []

    for row in listaDeDisparosRestada:
        row = list(row)
        row[0] = row[0] + 1
        row[1] = row[1] + 1
        listaSobrevivientesSumada.append(row)
    return listaSobrevivientesSumada
#sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
def botesSobrevivientes(mapaBase, listaDeDisparosRestada):
    for i in range(len(mapaBase)):
        for n in range(len(mapaBase)):
            for j in range(len(listaDeDisparosRestada)):
                for m in range(len(listaDeDisparosRestada)):
                    posicionEnMapa = [i,n]
                    posicionEnDisparos = [j,m]
                    if posicionEnMapa == posicionEnDisparos:
                        duplicado = posicionEnDisparos
                        listaDeDisparosRestada.remove(duplicado)
                    else:
                        continue
    return listaDeDisparosRestada

def ejercicio2(mapa,listaDeTuplas):
    restarNumeroDeIndice(listaDeTuplas)
    listaDeDisparosRestada = restarNumeroDeIndice(listaDeTuplas)

    posicionesDeBarcos(mapa)
    mapaBase = posicionesDeBarcos(mapa)

    botesSobrevivientes(mapaBase, listaDeDisparosRestada)
    listaDeDisparosRestada = botesSobrevivientes(mapaBase, listaDeDisparosRestada)

    sumarNumeroDeIndice(listaDeDisparosRestada)
    listaSobrevivientesSumada = sumarNumeroDeIndice(listaDeDisparosRestada)

    return listaSobrevivientesSumada


posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])
