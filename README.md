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

## 📁 Project Structure

Gradebook-Analyzer/
│── gradebook.py
│── Readme.md
└── marks.csv


---

## ▶️ How to Run

### 🔹 Manual Input Mode

Run the program:
```bash
python gradebook.py
1. Manual Input
2. CSV Input
,,,bash
###Your marks.csv file should follow this format:
mahesh,89
suresh,78
nilesh,67
rakesh,56
rana,45
billu,34

🧪 Error Handling

The program safely handles:

❌ Invalid integers

❌ Marks outside the range 0–100

❌ Missing CSV file

❌ Invalid or corrupted CSV lines

👨‍💻 Author

Prithvee Singh Yadav

⭐ Note

This project is ideal for beginners learning:

Python basics

File handling

Lists & dictionaries

Statistics

Input validation

Real-world console application structure
