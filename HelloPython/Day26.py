"""
Day 26 — Error Handling in File Operations
Problem:
=======
1. Try to open a file that doesn't exist. Handle the FileNotFoundError gracefully.
2. Write a function safe_read(filename) that returns file contents or a friendly error message.
3. Write a function safe_write(filename, data) that catches permission or OS errors.
4. Create a log file errors.log. Every time an error occurs in your program, append a timestamped message to the log.
5. Demonstrate all error scenarios by intentionally triggering them and showing the log.
   Concepts: try/except/finally, multiple exception types, datetime for timestamps
"""
import logging
from pathlib import Path

#4
logging.basicConfig(
    filename="errors.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
    )

# 1 & 2
def safe_read(filename):
    try:
        with open(filename, 'r') as log:
            return log.read()
    except FileNotFoundError as e:
        logging.error(f"Failed to read '{filename}' : {e}")
        return "File not found, Please enter a valid file name"

#print(safe_read("log.txt"))
#print(safe_read("library.json"))

# 3
def safe_write(filename, data):
    try:
        with open(filename, 'w') as log:
            log.write(data)
    except PermissionError as p:
        logging.error(f"You do not have permission to write to '{filename}' : {p}")
    except FileNotFoundError as f:
        logging.error(f"File Name : '{filename}' Not Found : {f}")
        #print("File not found, Please enter a valid file name")
    except OSError as o:
        logging.error(f"OS Error Triggered For : '{filename}' : {o}")
        print("File not found, Please enter a valid file name")

safe_write("write.txt", safe_read("library.json"))   #successful run
#safe_write("write.txt", safe_read("test.json"))  #Checking exception