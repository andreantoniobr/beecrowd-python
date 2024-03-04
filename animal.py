p1 = input()
p2 = input()
p3 = input()
data = [p1, p2, p3]

animals = {
    "aguia": ["vertebrado", "ave", "carnivoro"],
    "pomba": ["vertebrado", "ave", "onivoro"],
    "homem": ["vertebrado", "mamifero", "onivoro"],
    "vaca":  ["vertebrado", "mamifero", "herbivoro"],
    "pulga":       ["invertebrado", "inseto", "hematofago"],
    "lagarta":     ["invertebrado", "inseto", "herbivoro"],
    "sanguessuga": ["invertebrado", "anelideo", "hematofago"],
    "minhoca":     ["invertebrado", "anelideo", "onivoro"]
}

def try_get_animal_name(data) -> str:
    can_get_animal_name = False
    animal_name = ""
    for key, animal_data in animals.items():
        if animal_data == data:
            animal_name = key
            can_get_animal_name = True
            break
    return can_get_animal_name, animal_name 

can_get_animal_name, animal_name = try_get_animal_name(data)

if can_get_animal_name:
    print(animal_name)
else:
    print("None")