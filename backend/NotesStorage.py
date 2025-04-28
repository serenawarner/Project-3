import json
import os
from datetime import datetime

NOTES_DIR = "notes_data"
os.makedirs(NOTES_DIR, exist_ok=True)

def _get_note_filename(group_id: str, date: str = None) -> str:
    """Generate a filename based on group and optional date."""
    date = date or datetime.now().strftime("%Y-%m-%d")
    return os.path.join(NOTES_DIR, f"{group_id}_{date}.json")

def save_note(group_id: str, note: str, user: str) -> None:
    """Append a new note to the group's file."""
    filename = _get_note_filename(group_id)
    data = {"user": user, "note": note, "timestamp": datetime.now().isoformat()}

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            notes = json.load(f)
    else:
        notes = []

    notes.append(data)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

def get_notes(group_id: str, date: str = None) -> list:
    """Retrieve all notes for a group on a specific date."""
    filename = _get_note_filename(group_id, date)
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def search_notes_backend(keyword: str) -> list:
    """
    Search all saved notes in the backend folder for a given keyword.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        list: A list of filenames that contain the keyword.
    """
    matching_files = []
    keyword = keyword.lower()

    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(NOTES_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                notes = json.load(file)
                for note in notes:
                    if keyword in note.get("note", "").lower():
                        matching_files.append(filename)
                        break  

    print(f"Found {len(matching_files)} file(s) with the keyword '{keyword}'.")
    for name in matching_files:
        print(f" - {name}")

    return matching_files

if __name__ == "__main__":
    keyword = input("Enter a keyword to search: ")
    search_notes_backend(keyword)


