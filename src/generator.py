import numpy as np
import random

def generate_timetable(sec, teacher_courses):
    sections_list = sec
    teacher_courses_list = teacher_courses
    courses_list = [[i[1]] for i in teacher_courses_list]
    teachers_list = [[i[0]] for i in teacher_courses_list]
    courses_with_no_list = [[i[1], 5] for i in teacher_courses_list]  #minimum number of classes

    sections = []
    courses = []
    teachers = []
    for i in range(0,len(sections_list)):
        sections.append(sections_list[i][0])
    for i in range(0,len(courses_list)):
        courses.append(courses_list[i][0])
        teachers.append(teachers_list[i][0])
    courses_set = list(set(courses))

    #All subjects with number of how many times it will be studied in a week
    subjects_no_dict = {}
    for i in range(0,len(courses_set)):
        for j in range(0,len(courses_with_no_list)):
            if courses_with_no_list[j][0] == courses_set[i]:
                subjects_no_dict[courses_set[i]] = int(courses_with_no_list[j][1])
                break

    #teachers with theirs subjects as a Dictionary
    teachers_with_subjects = {}
    for i in range(0,len(teacher_courses_list)):
        teachers_with_subjects[teacher_courses_list[i][0]] = teacher_courses_list[i][1]

    #availablity of teachers
    teachers_with_week_duties = {}
    for i in range(0,len(teachers)):
        array=[[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0]]
        teachers_with_week_duties[teachers[i]] = array

    all_classes_timetable_array = []
    for clas in range(0,len(sections)):
        # 5 days and 7 timeslots
        timetable_matrix = np.empty([5, 8] , dtype=object)
        for i in range(0,5):
            timetable_matrix[i,5] = "Lunch Break"
            timetable_matrix[i,2] = "Short Break"

        #courses with no per week
        courses_no_per_week = {}
        for j in range(0,len(courses_set)):
            courses_no_per_week[courses_set[j]] = subjects_no_dict[courses_set[j]]

        print("Weekly Time Table for class: ",sections[clas])
        for day in range(0,5):
            if all(value == 0 for value in courses_no_per_week.values()):
                break
            else:
                day_courses = []
                for time_slot in range(0,8):
                    if all(value == 0 for value in courses_no_per_week.values()):
                        break
                    else:
                        if time_slot == 2:
                            day_courses.append("Short Break")
                        elif time_slot == 5:
                            day_courses.append("Lunch Break")
                        else:
                            random.shuffle(courses_set)
                            for r in range(0,len(courses_set)):
                                random_course = courses_set[r]
                                if(random_course in day_courses or courses_no_per_week[random_course]==0):
                                    #print(random_course)
                                    continue
                                else:
                                    teachers_list = []
                                    instructor =""
                                    for teacher, subject in teachers_with_subjects.items():
                                        if subject == random_course:
                                            teachers_list.append(teacher)
                                    for t in range(0,len(teachers_list)):
                                        if(teachers_with_week_duties[teachers_list[t]][day][time_slot]==0):
                                            instructor = teachers_list[t]
                                            teachers_with_week_duties[teachers_list[t]][day][time_slot]=1
                                            break
                                        else:
                                            continue
                                    if(instructor==""):
                                        continue
                                    else:
                                        day_courses.append(random_course)
                                        courses_no_per_week[random_course] = courses_no_per_week[random_course] - 1
                                        timetable_matrix[day][time_slot] = random_course+":" + instructor
                                        break
        all_classes_timetable_array.append(timetable_matrix)
    return all_classes_timetable_array