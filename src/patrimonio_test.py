from patrimonio import *

def test_lee_bienes(archivo):
    return lee_bienes(archivo)

def test_calcula_paises(datos):
    return calcula_paises(datos)

def test_bienes_por_tipo(datos, tipo):
    return bienes_por_tipo(datos)[tipo]

def test_dibuja_bienes_por_tipo(datos):
    return dibuja_bienes_por_tipo(datos)

def test_pais_mas_bienes(datos):
    return pais_mas_bienes(datos)

def test_bienes_mas_recientes_por_pais(datos):
    return bienes_mas_recientes_por_pais(datos)

def main():
    DATOS = test_lee_bienes('./data/whs.csv')
    print(DATOS[:3])
    print(test_calcula_paises(DATOS))
    print(test_bienes_por_tipo(DATOS, 'Mixed'))
    print(test_dibuja_bienes_por_tipo(DATOS))
    print(test_pais_mas_bienes(DATOS))
    print(test_bienes_mas_recientes_por_pais(DATOS))

if __name__ == '__main__':
    main()