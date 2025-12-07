"""
Name: Prithvee Singh Yadav
roll_number: 2501010087
Title: "Gradebook Analyzer"
"""

import csv


def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    if not marks_dict:
        return 0

    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2

    return scores[mid] if n % 2 != 0 else (scores[mid - 1] + scores[mid]) / 2


def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0


def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0


def save_to_csv(marks_dict, filename="marks.csv"):
     #Overwrite marks.csv with the current marks_dict.
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for name, marks in marks_dict.items():
                writer.writerow([name, marks])
        print(" Data saved to marks.csv")
    except Exception as e:
        print(f" Could not save to marks.csv: {e}")


def load_from_csv(filename="marks.csv"):
    # Read marks from CSV and return a dictionary.
    marks_dict = {}
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                name = row[0]
                marks = int(row[1])
                if 0 <= marks <= 100:
                    marks_dict[name] = marks
                else:
                    print(f"Error: Invalid marks ({marks}) for {name} in CSV. Must be 0–100.")
    except FileNotFoundError:
        print("Error: 'marks.csv' file not found.")
    except ValueError:
        print("Error: CSV contains invalid (non-integer) data.")
    return marks_dict


def main():
    print("Welcome! This is a program to easily analyse student grades.\n")

    while True:
        print("\n=== Gradebook Menu ===")
        print("1. Manual Input")
        print("2. CSV Input")
        print("3. Exit Program")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Error: Please enter a number.")
            continue

        if choice == 3:
            print("Exiting Gradebook Analyzer. Goodbye!")
            break

        if choice not in (1, 2):
            print("Error: Invalid Input. Please select 1, 2, or 3.")
            continue

        marks_dict = {}

        #MANUAL INPUT
        if choice == 1:
            try:
                n = int(input("Enter number of students: "))
                for i in range(1, n + 1):
                    name = input(f"Enter name for student {i}: ")

                    while True:
                        try:
                            marks = int(input(f"Enter marks for {name} (0–100): "))
                            if 0 <= marks <= 100:
                                break
                            else:
                                print("Error: Marks must be between 0 and 100.")
                        except ValueError:
                            print("Error: Marks must be an integer.")

                    marks_dict[name] = marks

            except ValueError:
                print("Error: Please enter a valid number.")
                continue

            # 🔹 Save manual input to CSV
            save_to_csv(marks_dict)

        #CSV INPUT
        elif choice == 2:
            marks_dict = load_from_csv()

        # If still empty, nothing to analyse
        if not marks_dict:
            print("\nNo data to analyse (marks list is empty).")
            continue

        #ANALYSIS
        print("\n--- Analysis ---")
        print(f"Average:\t{calculate_average(marks_dict):.2f}")
        print(f"Median:\t\t{calculate_median(marks_dict)}")
        print(f"Max Score:\t{find_max_score(marks_dict)}")
        print(f"Min Score:\t{find_min_score(marks_dict)}")

        #GRADE ASSIGNMENT
        grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        student_grades = {}

        for name, marks in marks_dict.items():
            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            else:
                grade = "F"

            grades[grade] += 1
            student_grades[name] = grade

        print("\nGrades\t\tTotal Students")
        for grade, count in grades.items():
            print(f"{grade}\t\t{count}")

        #PASS / FAIL 
        passed = [n for n, m in marks_dict.items() if m >= 40]
        failed = [n for n, m in marks_dict.items() if m < 40]

        print("-" * 35)
        print(f"Total Passed Students: {len(passed)}")
        print(f"Names: {', '.join(passed) if passed else 'None'}")

        print(f"Total Failed Students: {len(failed)}")
        print(f"Names: {', '.join(failed) if failed else 'None'}")

        #RESULTS TABLE 
        print("\nName\t\tMarks\t\tGrade")
        print("-" * 35)
        for name, marks in marks_dict.items():
            print(f"{name}\t\t{marks}\t\t{student_grades[name]}")

        print("\n" + "=" * 35 + "\n")


main()