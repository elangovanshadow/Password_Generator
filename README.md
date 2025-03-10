# 🔐 Password Manager with Password Generator

![Logo](logo.png)

A simple desktop application built with Python and Tkinter to securely store and generate passwords.  
This tool helps you manage website credentials and create strong, random passwords easily.

---

## 🎮 Features

- Generate random, secure passwords with letters, numbers, and symbols.
- Save website credentials (Website, Email/Username, Password) to a CSV file.
- Simple and intuitive graphical user interface (GUI) using Tkinter.
- Copy generated passwords directly to the clipboard.
- Pre-fills email/username for faster entry.
- Includes a **logo.png** displayed in the application UI for a polished look.

---

## 📝 Files Included

| File             | Description                                                             |
|------------------|-------------------------------------------------------------------------|
| `main.py`        | Main script containing the application logic and GUI using Tkinter      |
| `logo.png`       | Logo displayed in the GUI (place it in the same directory as `main.py`) |
| `data.csv`       | CSV file that stores website credentials (Website, Email, Password)     |

---

## ▶️ How to Run the Application

1. Make sure you have **Python 3.x** installed on your computer.
2. Install the **required libraries**:
   - Tkinter (comes pre-installed with Python)
   - Pandas
   - Pyperclip (for copying password to clipboard)

   Run the following command to install dependencies (if needed):
   ```bash
   pip install pandas pyperclip
