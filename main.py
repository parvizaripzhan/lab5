import collections
string = input("1.1)буквалар: ")
ch_list = list(string)
print(ch_list)
print("1.2)буквалар неше рет кездесет")
san = collections.Counter(string)
print(san)


#san = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#']
print("TASK1.3")

list_vow = []
list_cons = []
list_symb = []

for char in san:
    if char in ['a','e','i','o','u']:
        list_vow.append(char)
    elif char.isalpha():
        list_cons.append(char)
    else:
        list_symb.append(char)

#print("Initial List: ", san)
print("List Vow: ", list_vow)
print("List Cons: ", list_cons)
print("List Symbols: ", list_symb)
print()


print("task1.4")
def divide_into_quartiles(list_A):
    sorted_list = sorted(list_A)
    n = len(sorted_list)
    q1 = sorted_list[:n // 4]
    q2 = sorted_list[n // 4: 2 * (n // 4)]
    q3 = sorted_list[2 * (n // 4): 3 * (n // 4)]
    q4 = sorted_list[3 * (n // 4):]

    return q1, q2, q3, q4

list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 5]

q1, q2, q3, q4 = divide_into_quartiles(list_A)

print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)
#print(list_A)


print("task 2.1")
def create_student_dict(name, assignment_scores, lab_scores, test_scores):
    student_dict = {}
    student_dict['Name'] = name
    student_dict['Assignment Scores'] = assignment_scores
    student_dict['Lab Scores'] = lab_scores
    student_dict['Test Scores'] = test_scores
    return student_dict

student1 = create_student_dict('Adam', [82, 56, 44, 30], [78, 77], [78.2, 77.2])
print(student1)
print("task 2.2")
def check_submission(student_dict):
    submission_check = {}
    for student in student_dict:
        if len(student_dict[student]['Assignment Scores']) == 4 and len(student_dict[student]['Lab Scores']) == 2 and len(student_dict[student]['Test Scores']) == 2:
            submission_check[student] = 6
        else:
            submission_check[student] = len(student_dict[student]['Assignment Scores']) + len(student_dict[student]['Lab Scores']) + len(student_dict[student]['Test Scores'])
    return submission_check

student_dict = {
    'Adam': {'Name': 'Adam', 'Assignment Scores': [82, 56, 44, 30], 'Lab Scores': [78, 77], 'Test Scores': [78.2, 77.2]},

}
submission_check = check_submission(student_dict)
print(submission_check)

print("task 2.3")
def calculate_final_grade(student_dict):
    final_grades = {}
    for student in student_dict:
        if len(student_dict[student]['assignment']) >= 4 and len(student_dict[student]['lab']) >= 2 and len(student_dict[student]['test']) >= 2:
            assignment_average = sum(student_dict[student]['assignment']) / len(student_dict[student]['assignment'])
            lab_average = sum(student_dict[student]['lab']) / len(student_dict[student]['lab'])
            test_average = sum(student_dict[student]['test']) / len(student_dict[student]['test'])
            final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
            final_grades[student] = final_grade
        else:
            final_grades[student] = 0
    return final_grades

student_dict = {
    'Adam': {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'lab': [78.2, 77.2], 'test': [78, 77]}
}
final_grades = calculate_final_grade(student_dict)
student_dict['Adam']['final_grade'] = final_grades['Adam']
print(student_dict)
print("task 2.4")
def create_nested_dict(student_dict):
    nested_dict = {}
    for student in student_dict:
        if 'final_grade' in student_dict[student]:
            nested_dict[student_dict[student]['name']] = {'Assignment Scores': student_dict[student]['assignment'], 'Lab Scores': student_dict[student]['lab'], 'Test Scores': student_dict[student]['test'], 'Final Grade': student_dict[student]['final_grade']}
    return nested_dict

student_dict = {
    'Adam': {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'lab': [78.2, 77.2], 'test': [78, 77], 'final_grad
