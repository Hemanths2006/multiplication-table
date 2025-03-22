# Multiplication Table Generator & Viewer

## 📌 Overview
This Python program allows users to **generate** and **retrieve** multiplication tables. The tables are saved in text files, and users can access them later.

## 🚀 Features
- ✅ Generate a multiplication table and save it to a `.txt` file.
- ✅ Retrieve and display saved multiplication tables.
- ✅ Handles invalid inputs (non-numeric values, missing files, etc.).
- ✅ User-friendly interface with clear instructions.
- ✅ Exit option for quitting the program gracefully.

## 🛠️ Requirements
- Python 3.x

## 📥 Installation
1. Clone this repository or download the script.
   ```sh
   git clone https://github.com/your-repo/multiplication-table.git
   cd multiplication-table
   ```
2. Ensure you have Python installed. You can check by running:
   ```sh
   python --version
   ```

## ▶️ Usage
Run the script using Python:
```sh
python script.py
```

### Menu Options:
1️⃣ **Generate Multiplication Table** → Enter a number, and the program will generate and save the multiplication table.
2️⃣ **Show Multiplication Table** → Enter a number to retrieve and display a previously saved table.
3️⃣ **Exit** → Closes the program.

### Example Run
```
🌟 Main Menu 🌟
1️⃣ Generate Multiplication Table
2️⃣ Show Multiplication Table
3️⃣ Exit
➡️ Enter your choice (1, 2, or 3): 1
Enter a number to generate its multiplication table: 5

🔢 Multiplication Table of 5:

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

✅ Multiplication table saved as '5_multiplication_table.txt'.
```

## 📂 File Format
Generated tables are stored as text files in the format:
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

## ⚠️ Error Handling
- **Invalid input** → Displays an error message instead of crashing.
- **File not found** → Informs the user if a requested table doesn't exist.

## 📜 License
This project is licensed under the MIT License.

---

🚀 **Happy Coding!** 🎯


