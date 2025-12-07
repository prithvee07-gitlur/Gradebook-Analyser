# 📊 Gradebook Analyzer (Python)

The **Gradebook Analyzer** is a Python console application that analyzes student marks, assigns grades, computes statistics, and supports both **manual input** and **CSV file input**. It is designed for quick academic data analysis with proper validation and formatted output.

---

## 🚀 Features

- ✅ Manual input mode with validation (0–100 marks)  
- ✅ CSV input mode (`marks.csv`)  
- ✅ Automatically calculates:
  - Average  
  - Median  
  - Maximum score  
  - Minimum score  
- ✅ Assigns grades (A–F)  
- ✅ Displays:
  - Pass list  
  - Fail list  
- ✅ Shows a formatted results table  

---
## 📂 Project Structure

* **Gradebook_Analyzer.py:** The main Python script that contains the logic for processing grades.
* **marks.csv:** The input data file containing student names and their corresponding marks.

## 🚀 How to Run

* **Prerequisites:** Ensure you have Python 3.x installed on your system.
* **Setup:** Place `Gradebook_Analyzer.py` and `marks.csv` in the same directory.
* **Execution:** Open your terminal in the project folder and run the command `python Gradebook_Analyzer.py`.

## 🛠️ Usage

When you run the program, it performs the following actions automatically:

1.  **Read File:** The program looks for `marks.csv` in the current folder.
2.  **Process Data:** It parses the CSV to extract student names and scores.
3.  **Display Report:** It prints a summary to the console, including:
    * Total number of students.
    * Class average score.
    * Highest and lowest scores with student names.
    * A list of all students with their assigned letter grades.

## 👤 Author

**Prithvee Singh Yadav**
* **Roll No:** 2501010087
* **Project:** Gradebook Analyzer
