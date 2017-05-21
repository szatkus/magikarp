from database import Folder, Folder_Document_Link, Document, db
from application import application
import jsonpickle
from flask import Flask, render_template
import json
from collections import defaultdict

@application.route('/folders')
def folders():
    return render_template('folders.html')

@application.route('/folders_json')
def folders_json():
    wynik = defaultdict(list)
    
    instances = db.session.query(Folder, Document).outerjoin(Folder_Document_Link, Folder_Document_Link.folder_id == Folder.folder_id).outerjoin(Document, Document.document_id == Folder_Document_Link.document_id).all() # lista
    for instance in instances:
        if instance[0].__dict__['folder_id'] != -1:
            wynik[instance[0].__dict__['parent_folder_id']].append(instance[0])
        if instance[1] != None:
            wynik[instance[0].__dict__['parent_folder_id']].append(instance[1])
    
    return jsonpickle.encode(wynik)
