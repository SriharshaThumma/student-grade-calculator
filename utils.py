def get_marks():
    marks = []

    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    return marks