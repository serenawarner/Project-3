from FolderModel import notebook_db, Folder, Note, notebook
from NotesStorage import save_note
from datetime import datetime

def store_note_db(folder_tag: str, filepath: str, user: str) -> None:
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("Note file is empty.")
        
        note_title = lines[0].strip()
        note_content = ''.join(lines[1:]).strip()

    with notebook.app_context():
        # Find or create the folder
        folder = Folder.query.filter_by(tag=folder_tag).first()
        if not folder:
            folder = Folder(tag=folder_tag, name=folder_tag.capitalize())
            notebook_db.session.add(folder)
            notebook_db.session.commit()

        # Create the note in the database
        note = Note(title=note_title, content=note_content, folder=folder)
        notebook_db.session.add(note)
        notebook_db.session.commit()

        # Save the note to a JSON file
        save_note(group_id=folder_tag, note=note_content, user=user)
