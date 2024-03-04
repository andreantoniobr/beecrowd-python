ddd = int(input())
citys = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

def try_get_city_name_by_ddd(ddd:int):
    can_get_city_name = False
    city_name = ""
    for key, value in citys.items():
        if ddd == key:
            can_get_city_name = True
            city_name = value
            break
    return can_get_city_name, city_name

can_get_city_name, city_name = try_get_city_name_by_ddd(ddd)
if can_get_city_name:
    print(city_name)
else:
    print("DDD nao cadastrado")