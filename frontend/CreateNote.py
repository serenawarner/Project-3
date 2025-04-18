

file_path = "notes.txt"
    
def create_note():
    note = input("Enter your note:")
    print (f"Your note is: {note}")
    with open(file_path, "a") as file:
        file.write(note + "\n")
    print("note has been created")

def read_notes():
    with open(file_path, "r") as file:
        notes = file.readlines()
    for note in notes:
        print(note.strip())

def delete_note():
    note_to_delete = input("Enter the note you want to delete:")
    with open(file_path, "r") as file:
        notes = file.readlines()
    with open(file_path, "w") as file:
        for note in notes:
            if note.strip() != note_to_delete:
                file.write(note)
    print("Note has been deleted.")

if __name__ == "__main__":
    create_note()

