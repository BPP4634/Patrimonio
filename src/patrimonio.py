from collections import namedtuple
import csv
from matplotlib import pyplot as plt

Bien = namedtuple('Bien', 'code, name, year, category, country')

def lee_bienes(archivo):
    bienes = []
    with open(archivo, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for code, name, year, category, country in lector:
            code = int(code)
            year = int(year)
            bienes.append(Bien(code, name, year, category, country))
        return bienes

def calcula_paises(bienes):
    paises = set()
    for bien in bienes:
        paises.add(bien.country)
    return paises

def bienes_por_tipo(bienes):
    cultural = []
    natural = []
    mixed = []
    for bien in bienes:
        if bien.category == 'Cultural':
            cultural.append(bien)
        elif bien.category == 'Natural':
            natural.append(bien)
        else:
            mixed.append(bien)
    bpt={'Natural': natural, 'Cultural': cultural, 'Mixed': mixed}
    return bpt

def dibuja_bienes_por_tipo(bienes):
    bpt = bienes_por_tipo(bienes)
    numero_bienes= []
    for tipo in bpt:
        numero_bienes.append(len(bpt[tipo]))
    tipos = list(bpt.keys())
    plt.barh(range(len(numero_bienes)), numero_bienes, tick_label=tipos)
    plt.show()

def pais_mas_bienes(bienes, tipo='Cultural'):
    result = dict()
    for bien in bienes:
        if bien.category == tipo:
            if not bien.country in result:
                result[bien.country] = [bien]
            else:
                result[bien.country] += [bien]
    for pais in result:
        result[pais] = [len(result[pais])]
    result = list(result.items())
    return max(result, key = lambda b: b[1])

def bienes_mas_recientes_por_pais(bienes, n=3):
    result = dict()
    for bien in bienes:
        if not bien.country in result:
            result[bien.country] = [(bien.year,bien.name)]
        else:
            result[bien.country] += [(bien.year,bien.name)]
    for pais in result:
        result[pais] = sorted(result[pais], reverse=True)[:n]
    return result


'''SOLO MOSTRAR LOS N PRIMEROS: return dict(list(result.items())[:n])'''