

file_path = "notes.txt"
    
def create_note():
    note = input("Enter your note:")
    print (f"Your note is: {note}")
    with open(file_path, "a") as file:
        file.write(note + "\n")
    print("note has been created")


if __name__ == "__main__":
    create_note()