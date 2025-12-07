import csv

"""
Name: Prithvee Singh Yadav
Date: 25010100871
Title: "Gradebook Analyzer" 
"""

def calculate_average(marks_dict):
    """
    Calculates the arithmetic mean of the marks.
    Args: marks_dict (dict): Student names and marks
    Returns: average score (float)
    """
    if not marks_dict:
        return 0
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def calculate_median(marks_dict):
    """
    Calculates the median of the marks.
    Args: marks_dict (dict): Student names and marks
    Returns: median score (float)
    """
    if not marks_dict:
        return 0
    
    # Extract the marks into a list
    scores = list(marks_dict.values())
    # Sort the list
    scores.sort()
    
    n = len(scores)
    mid = n // 2
    
    # If odd length, take the middle element
    if n % 2 != 0:
        return scores[mid]
    # If even length, average the two middle elements
    else:
        return (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks_dict):
    """
    Finds the highest score out of the marks.
    Args: marks_dict (dict): Student names and marks
    Returns: maximum score (int)
    """
    if not marks_dict:
        return 0
    return max(marks_dict.values())

def find_min_score(marks_dict):
    """
    Finds the lowest score out of the marks.
    Args: marks_dict (dict): Student names and marks
    Returns: minimum score (int)
    """
    if not marks_dict:
        return 0
    return min(marks_dict.values())

def main():
    """
    Main function for driving the entire logic
    """
    # <--- TASK 2 --->
    while True:
        print("\n=== Gradebook Menu ===")
        print("1. Manual Input")
        print("2. CSV Input")
        print("3. Exit Program")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Error: Please enter a number.")
            continue # Skip to the next iteration of the loop

        # <--- EXIT LOGIC --->
        if choice == 3:
            print("Exiting Gradebook Analyzer. Goodbye!")
            break # Break out of the while loop
        
        if choice not in (1, 2):
            print("Error: Invalid Input. Please select 1, 2, or 3.")
            continue

        marks_dict = {}

        if choice == 1:
            try:
                n = int(input("Enter the number of students: "))
                for i in range(n):
                    name = input(f"Enter name for student {i+1}: ")
                    marks = int(input(f"Enter marks for {name}: "))
                    marks_dict[name] = marks
            except ValueError:
                print("Error: Marks must be integers.")
                continue # Restart loop on error

        elif choice == 2:
            try:
                with open("marks.csv", "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row: 
                            name = row[0]
                            marks = int(row[1]) 
                            marks_dict[name] = marks
            except FileNotFoundError:
                print("Error: 'marks.csv' file not found.")
                continue
            except ValueError:
                 print("Error: CSV contains invalid data.")
                 continue

        # <----- TASK 3: Statistics ----->
        print("\n--- Analysis ---")
        print(f"Average:\t{calculate_average(marks_dict)}") 
        print(f"Median:\t\t{calculate_median(marks_dict)}")
        print(f"Max Score:\t{find_max_score(marks_dict)}")
        print(f"Min Score:\t{find_min_score(marks_dict)}")
        
        # <----- TASK 4: Grade Assignment ----->
        grades = {}
        a, b, c, d, f = 0, 0, 0, 0, 0
        
        for name in marks_dict:
            grade = ""
            marks = marks_dict[name]
            if marks >= 90:
                grade = "A"
                a += 1
            elif marks >= 80:
                grade = "B"
                b += 1
            elif marks >= 70:
                grade = "C"
                c += 1
            elif marks >= 60:
                grade = "D"
                d += 1
            else:
                grade = "F"
                f += 1
            grades[name] = grade
        
        print("\nGrades\t\tTotal Students")
        print(f"A\t\t{a}\nB\t\t{b}\nC\t\t{c}\nD\t\t{d}\nF\t\t{f}")
            
        # <----- TASK 5: Pass/Fail Filter ----->
        # Using list comprehension logic
        passed_students = [x for x in marks_dict if marks_dict[x] >= 40]
        failed_students = [x for x in marks_dict if marks_dict[x] < 40]
        
        print("-" * 35)
        print(f"Total Passed Students: {len(passed_students)}")
        print(f"Names: {', '.join(passed_students)}")
        print(f"Total Failed Students: {len(failed_students)}")
        print(f"Names: {', '.join(failed_students)}")
        
        # <----- TASK 6: Results Table and Loop ----->
        print("\nName\t\tMarks\t\tGrade")
        print("-" * 35)
        for name, marks in marks_dict.items():
            print(f"{name}\t\t{marks}\t\t{grades[name]}")
        
        print("\n" + "="*35 + "\n") # Separator before next loop

print("Welcome! This is a program to easily analyse student grades.")
main()