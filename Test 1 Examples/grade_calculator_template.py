HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Step1: Get the student type
# If the student type is not UG, G, or DL,
# print an error message and exit the program
# Otherwise, continue with the program

student_type = input()
if student_type not in ("UG", "G", "DL"):
    print("Error: student status must be UG, G or DL")
else:
    # Step 2: Get the student grades

    # 600.0  300.0  120.0  185.0
    # input() -> "600.0  300.0  120.0  185.0"
    # input.split() -> ["600.0", "300.0", "120.0", "185.0"]
    # [float(x) for x in input().split()] -> [600.0, 300.0, 120.0, 185.0]

    student_grades = [float(x) for x in input().split()]

    # Step 3: Define the total points in each category,
    # and the weights for each student type

    total_points = (HOMEWORK_MAX, QUIZZES_MAX, MIDTERM_MAX, FINAL_MAX)
    ug_weights = (0.20, 0.20, 0.30, 0.30)
    g_weights = (0.15, 0.05, 0.35, 0.45)
    dl_weights = (0.05, 0.05, 0.40, 0.50)

    # Step 4: Calculate the percentages in each category

    student_percentages = []
    for i in range(len(student_grades)):
        student_percentages.append(min(100.0*student_grades[i]/total_points[i],100.0))


    # Step 5: Calculate the overall grade

    final_grade = 0.0
    for i in range(len(student_grades)):
        if student_type == 'UG':
            final_grade += student_percentages[i] * ug_weights[i]
        elif student_type == "G":
            final_grade += student_percentages[i] * g_weights[i]
        else:
            final_grade += student_percentages[i] * dl_weights[i]

    # Step 6: Calculate the letter grades

    if final_grade >= 90:
        letter = 'A'
    elif final_grade >= 80:
        letter = 'B'
    elif final_grade >= 70:
        letter = 'C'
    elif final_grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    # Step 7: Create the output report


