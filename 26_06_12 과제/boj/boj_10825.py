# 10825번 (국영수)
def student_score():
    student_list = []
    input_student_num = int(input(f'입력할 학생의 수 : '))
    for _ in range(input_student_num):
        student = input(f'이름과 국영수 성적을 차례대로 입력하시오 : ').split()
        student_list.append(student)

    student_list.sort(key=lambda score: (-int(score[1]), int(score[2]), -int(score[3]), score[0]))

    for s in student_list:
        print(s[0])

student_score()