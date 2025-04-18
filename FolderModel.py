from flask import Flask
from flask_sqlalchemy import SQLAlchemy

notebook = Flask(__name__)
notebook.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notebook.db'
notebook_db = SQLAlchemy(notebook)

#Plan for there to just be a single user so no user class necessary

class Folder(notebook_db.Model):
    id = notebook_db.Column(notebook_db.Integer, primary_key = True)
    tag = notebook_db.Column(notebook_db.String, nullable = False)     #identify individual folders
    name = notebook_db.Column(notebook_db.String, nullable = False)
    notes = notebook_db.relationship('Note', backref='folder', lazy = True)


class Note(notebook_db.Model):
    id = notebook_db.Column(notebook_db.Integer, primary_key = True)
    group_id = notebook_db.Column(notebook_db.String, nullable = False)
    title = notebook_db.Column(notebook_db.String, nullable = False)
    content = notebook_db.Column(notebook_db.Text) #import from createnote
    folder_id = notebook_db.Column(notebook_db.Integer, notebook_db.ForeignKey('folder.id'), nullable = False)



with notebook.app_context():

    notebook_db.drop_all()
    # Create all tables
    notebook_db.create_all()
    
    folder = Folder(tag="work-tag", name="Work")
    note = Note(group_id = "workywork", title="Student notes", content="Experienced pain", folder=folder)
    
    notebook_db.session.add(folder)
    notebook_db.session.add(note)
    notebook_db.session.commit()
    
    work_folder = Folder.query.filter_by(name="Work").first()
    #print(work_folder.notes)  # Returns all notes in the "Work" folder
    for note in work_folder.notes:
        print(f"Title: {note.title} | Content: {note.content}")


