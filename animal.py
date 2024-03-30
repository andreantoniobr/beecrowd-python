# Ex. Using only functios and condition structures.
# See animal_dictionary archive for dictionary use.

def is_vertebrate(animal_subphylum):
    return animal_subphylum == "vertebrado"

def is_invertebrate(animal_subphylum):
    return animal_subphylum == "invertebrado"

def is_bird(animal_class):
    return animal_class == "ave"

def is_insect(animal_class):
    return animal_class == "inseto"

def is_mammal(animal_class):
    return animal_class == "mamifero"

def is_annelid(animal_class):
    return animal_class == "anelideo"

def is_carnivore(animal_order):
    return animal_order == "carnivoro"

def is_herbivore(animal_order):
    return animal_order == "herbivoro"

def is_omnivorous(animal_order):
    return animal_order == "onivoro"

def is_hematophagous(animal_order):
    return animal_order == "hematofago"

def get_animal(animal_subphylum, animal_class, animal_order):
    if is_vertebrate(animal_subphylum) and is_bird(animal_class) and is_carnivore(animal_order):
        animal = "aguia"
    elif is_vertebrate(animal_subphylum) and is_bird(animal_class) and is_omnivorous(animal_order):
        animal = "pomba"
    elif is_vertebrate(animal_subphylum) and is_mammal(animal_class) and is_omnivorous(animal_order):
        animal = "homem"
    elif is_vertebrate(animal_subphylum) and is_mammal(animal_class) and is_herbivore(animal_order):
        animal = "vaca"
    elif is_invertebrate(animal_subphylum) and is_insect(animal_class) and is_hematophagous(animal_order):
        animal = "pulga"
    elif is_invertebrate(animal_subphylum) and is_insect(animal_class) and is_herbivore(animal_order):
        animal = "lagarta"
    elif is_invertebrate(animal_subphylum) and is_annelid(animal_class) and is_hematophagous(animal_order):
        animal = "sanguessuga"
    elif is_invertebrate(animal_subphylum) and is_annelid(animal_class) and is_omnivorous(animal_order):
        animal = "minhoca"
    else:
        animal = "none"
    return animal

def main():
    animal_subphylum  = input()
    animal_class = input()
    animal_order = input()
    print(get_animal(animal_subphylum, animal_class, animal_order)) 

main()   