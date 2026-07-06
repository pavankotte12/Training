# Appending text to log.txt

def append_log(message):
    try:
        with open("log.txt","r") as f:
            lines = f.readlines()
            line_num = len(lines) + 1
    
    except FileNotFoundError:
        line_num = 1
        
    with open("log.txt","a") as f:
            f.write(f"{line_num}.{message}\n")

append_log("Started program")
append_log("Loaded data")
append_log("Finished processing")

with open("log.txt","r") as f:
     contents = f.read()
     print(contents)