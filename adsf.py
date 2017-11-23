def disparoConMapaYListaDeTuplas(mapa, listaDeTuplas):

    mapaActualizado = []

    if mapa != [] and mapa != [""] and len(mapa) > 1:
        for fila in mapa:
            if not fila.isspace() and len(fila) == len(mapa[1]):
                for i in range (len(listaDeTuplas)):
                    if mapa[listaDeTuplas[i][0]][listaDeTuplas[i][1]] == "b":
                       mapa[listaDeTuplas[i][0]][listaDeTuplas[i][1]] == "."
                    return mapaActualizado
            else:
                return mapaActualizado
    else:
        return mapaActualizado

def restarNumeroDeIndice(listaDeTuplas):

    listaDeDisparosRestada = []

    for row in listaDeTuplas:
        row = list(row)
        row[0] = row[0] - 1
        row[1] = row[1] - 1
        listaDeDisparosRestada.append(row)
    return listaDeDisparosRestada


def sumarNumeroDeIndice(listaSobrevivientes):

    listaSobrevivientesSumada = []

    for row in listaSobrevivientes:
        row = list(row)
        row[0] = row[0] + 1
        row[1] = row[1] + 1
        listaSobrevivientesSumada.append(row)
    return listaSobrevivientesSumada

def botesSobrevivientes(mapaActualizado):
    listaDeBotesSobrevivientes = []
    for i in range(len(mapaActualizado)):
        for j in range(len(mapaActualizado)):
            if mapaActualizado[i][j] == "b":
                t = (i,j)
                listaDeBotesSobrevivientes.append(t)
        return listaSobrevivientes

def ejercicio2(mapa,listaDeTuplas):
    return disparoConMapaYListaDeTuplas(mapa, listaDeTuplas)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

#assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
#assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])