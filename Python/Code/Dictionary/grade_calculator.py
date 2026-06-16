# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }


students = [jack, james, dylan, jess, tom]


def student_average(marks_list):
    total_sum = sum(marks_list)


    return total_sum / len(marks_list)


def grade_cal(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

def class_avergae(student_list):
    result_avg_list = []
    for i in student_list:
        #print(i['name'], i['assignment'])
        assign_avg = student_average(i['assignment'])
        test_avg = student_average(i['test'])
        lab_avg = student_average(i['lab'])
        #print('Student name is ', i['name'], assign_avg, test_avg, lab_avg)
        cal =   0.1 * assign_avg + 0.7 * test_avg + 0.2 * lab_avg
        sub_list = [i['name'], cal]
        result_avg_list.append(sub_list)
    return result_avg_list

cal = class_avergae(students)
#print(cal)
a = 0
b = 1
while a < len(cal):
    #print(a)
    grade = grade_cal(int(cal[a][b]))
    print(cal[a][0], cal[a][b], grade)
    a = a + 1

#print('cal', cal[0][1])
# for j in cal:
#     grade = grade_cal(int(j))
#     print(grade)


