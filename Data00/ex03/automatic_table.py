from table import create_table
import os

def main():
    for file in os.listdir("../subject/customer"):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            create_table(os.path.join("../subject/customer", file), table_name)
    
if __name__ == "__main__":
    main()