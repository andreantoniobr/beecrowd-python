test_subjects_total = 0
rabbits_amount = 0
mouses_amount = 0
frogs_amount = 0

def get_percent(amount):
    return (amount * 100) / test_subjects_total

def is_rabbit(subject_type):
    return subject_type == "C"

def is_mouse(subject_type):
    return subject_type == "R"

def is_frog(subject_type):
    return subject_type == "S"

def print_result():
    print(f"Total: {test_subjects_total} cobaias")
    print(f"Total de coelhos: {rabbits_amount}")
    print(f"Total de ratos: {mouses_amount}")
    print(f"Total de sapos: {frogs_amount}")
    print(f"Percentual de coelhos: {get_percent(rabbits_amount):.2f} %")
    print(f"Percentual de ratos: {get_percent(mouses_amount):.2f} %")
    print(f"Percentual de sapos: {get_percent(frogs_amount):.2f} %")

def get_data(test_subjects_total, rabbits_amount, mouses_amount, frogs_amount):
    user_input_amount = int(input())
    for i in range(user_input_amount):
        data = input().split()
        test_subjects_amount = int(data[0])
        subject_type = data[1]

        if is_rabbit(subject_type) or is_mouse(subject_type) or is_frog(subject_type):
            test_subjects_total += test_subjects_amount
            if is_rabbit(subject_type):
                rabbits_amount += test_subjects_amount
            elif is_mouse(subject_type):
                mouses_amount += test_subjects_amount
            elif is_frog(subject_type):
                frogs_amount += test_subjects_amount

    return test_subjects_total, rabbits_amount, mouses_amount, frogs_amount

test_subjects_total, rabbits_amount, mouses_amount, frogs_amount = get_data(test_subjects_total, rabbits_amount, mouses_amount, frogs_amount)
print_result()