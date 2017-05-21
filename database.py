from flask_sqlalchemy import SQLAlchemy
from application import application

db = SQLAlchemy(application)

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80))

class Folder(db.Model):
    __tablename__ = 'FOLDER'
    folder_id = db.Column('FOLDER_ID', db.Integer, db.Sequence('folder_id_seq'), primary_key=True)
    parent_folder_id = db.Column('PARENT_FOLDER_ID', db.Integer, nullable=False)
    description = db.Column('DESCRIPTION', db.String(50), nullable=False)
    last_updated_timestamp = db.Column('LAST_UPDATED_TIMESTAMP', db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Document(db.Model):
    __tablename__ = 'DOCUMENT'
    document_id = db.Column('DOCUMENT_ID', db.Integer, db.Sequence('document_id_seq'), primary_key=True)
    document_name = db.Column('DOCUMENT_NAME', db.String(50), nullable=False)
    content = db.Column('CONTENT', db.String(150))
    last_updated_timestamp = db.Column('LAST_UPDATED_TIMESTAMP', db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Folder_Document_Link(db.Model):
    __tablename__ = 'FOLDER_DOCUMENT_LINK'
    folder_id = db.Column('FOLDER_ID', db.Integer, db.ForeignKey('FOLDER.FOLDER_ID'), primary_key=True)
    document_id = db.Column('DOCUMENT_ID', db.Integer, db.ForeignKey('DOCUMENT.DOCUMENT_ID'), primary_key=True)
    last_updated_timestamp = db.Column('LAST_UPDATED_TIMESTAMP', db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())   
