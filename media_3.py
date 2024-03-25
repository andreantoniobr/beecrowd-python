def get_weighted_average(n1, n2, n3, n4, p1, p2, p3, p4):
    average = 0
    p = p1 + p2 + p3 + p4
    if p > 0:
        average = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4) / p
    return average

def calc_new_average(previus_average):
    exam_note = float(input())
    average = (previus_average + exam_note) / 2
    return exam_note, average

def get_student_end_situation(previus_average):
    exam_note, average = calc_new_average(previus_average)
    print(f"Nota do exame: {exam_note:.1f}")
    if average >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {average:.1f}")

def process_student_situation(n1, n2, n3, n4, p1, p2, p3, p4):
    average = get_weighted_average(n1, n2, n3, n4, p1, p2, p3, p4)
    print(f"Media: {average:.1f}")
    if average > 7:
        print("Aluno aprovado.")
    elif average >= 5 and average <= 7:
        print("Aluno em exame.")
        get_student_end_situation(average)
    else:
        print("Aluno reprovado.")

def main():
    data = input().split()
    n1 = float(data[0])
    n2 = float(data[1])
    n3 = float(data[2])
    n4 = float(data[3])
    p1 = 2
    p2 = 3
    p3 = 4
    p4 = 1
    process_student_situation(n1, n2, n3, n4, p1, p2, p3, p4)       

main()