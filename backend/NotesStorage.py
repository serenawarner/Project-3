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