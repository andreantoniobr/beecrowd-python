# See ddd_dictionary for dictionary use.

def get_city_by_ddd(ddd):
    if ddd == 61:
        city = "Brasilia"
    elif ddd == 71:
        city = "Salvador"
    elif ddd == 11:
        city = "Sao Paulo"
    elif ddd == 21:
        city = "Rio de Janeiro"
    elif ddd == 32:
        city = "Juiz de Fora"
    elif ddd == 19:
        city = "Campinas"
    elif ddd == 27:
        city = "Vitoria"
    elif ddd == 31:
        city = "Belo Horizonte"
    else:
        city = "DDD nao cadastrado"
    return city

def main():
    ddd = int(input())
    print(get_city_by_ddd(ddd))

main()