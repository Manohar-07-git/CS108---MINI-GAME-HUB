import os

def clean_history():
    if not os.path.exists("history.csv"):
        print("No history.csv found.")
        return
        
    with open("history.csv", "r") as f:
        lines = f.readlines()
        
    cleaned_lines = 0
    with open("history.csv", "w") as f:
        for line in lines:
            # Only write the line back if it doesn't start with a python object reference
            if not line.startswith("<baseclass"):
                f.write(line)
            else:
                cleaned_lines += 1
                
    print(f"Cleaned up! Removed {cleaned_lines} corrupted rows.")

clean_history()