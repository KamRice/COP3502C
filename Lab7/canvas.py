from course_data import actual_data as actual_data


def main():
    tgt_student = input("Enter the student's name: ")
    tgt_student_grade = 0

    if tgt_student in actual_data["roster"]:
        for assignment in actual_data["assignments"]:
            print(f"{assignment}: {actual_data['assignments'][assignment]['submissions'].get(tgt_student, 0)}%")
            tgt_student_grade += actual_data['assignments'][assignment]['submissions'].get(tgt_student, 0) * (
                    actual_data['assignments'][assignment]['weight'] / 100)
        print(f"Total grade: {tgt_student_grade:.2f}%")
    else:
        print("Student not found.")


if __name__ == "__main__":
    main()
