from flask import request, jsonify
from FolderModel import notebook, notebook_db, Folder, Note
from notebook_interface import store_note_db
import os

@notebook.route('/')
def home():
    return "Notebook app is running!"


@notebook.route('/store-note', methods=['POST'])
def api_store_note():
    data = request.json
    folder_tag = data.get('folder_tag')
    filepath = data.get('filepath')
    user = data.get('user')
    date = data.get('note_creation_time')

    required_fields = [folder_tag, filepath, user, date]
#checks that the client is sending expected information and returns error if missing fields                          
    if not all(required_fields):                         #400 client side error
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:                                 #200 succesesful status code
        store_note_db(folder_tag=folder_tag, filepath=filepath, user=user)
        return jsonify({'status': 'Note stored successfully'}), 201
    except Exception as e:              #500 server side error
        return jsonify({'error': str(e)}), 500
    
@notebook.route('/welcome-page', methods = ['GET'])
def get_user():
    user = request.args.get('user')

    if not user:
        return jsonify({'error': 'Missing user'}), 400

    return welcome_page(user)

def welcome_page(user):
    return f'Welcome {user}'


@notebook.route('/retrieve-notes', methods=['GET'])
def retrieve_notes():
    notes = Note.query.all()
    return jsonify([
        {
            'title': note.title,
            'content': note.content,
            'folder': note.folder.tag,
            'date': note.date
        } for note in notes
        
    ])

if __name__ == '__main__':
    #should show running on default port: http://127.0.0.1:5000/
    notebook.run(debug=True)
