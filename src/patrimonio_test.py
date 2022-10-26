from patrimonio import *

DATOS = lee_bienes('./data/whs.csv')
print(DATOS[:3])
print(calcula_paises(DATOS))
bpt = (bienes_por_tipo(DATOS))
print(bpt['Mixed'])
dibuja_bienes_por_tipo(DATOS)
print(pais_mas_bienes(DATOS))
print(bienes_mas_recientes_por_pais(DATOS))