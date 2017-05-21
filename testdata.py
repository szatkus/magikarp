from database import *

session = db.session()

# usuniecie istniejacych rekordow
session.query(Folder).delete()
session.query(Document).delete()
session.query(Folder_Document_Link).delete()

session.add(Folder(folder_id = -1, parent_folder_id = -1, description='dummy root'))
session.add(Folder(parent_folder_id = -1, description='sprawy wazne i powazne'))
session.add(Folder(parent_folder_id = -1, description='zabawa i relaks'))
session.add(Folder(parent_folder_id = 1, description='bardzo wazne'))

session.add(Document(document_name = 'kody_do_GTA_VC.txt', content='FANNYMAGNET - Przyciagasz kobiety\nNOBODYLIKESME - wszyscy chca Cie zabic'))
session.add(Document(document_name = 'tajny_plik.txt', content='tajne'))

session.add(Folder_Document_Link(folder_id = -1, document_id = 1))
session.add(Folder_Document_Link(folder_id = -1, document_id = 2))

session.commit()

print(session.execute('select * from folder f left outer join folder_document_link fd on (fd.folder_id=f.folder_id) left outer join document d on (d.document_id=fd.document_id)').fetchall()) # sprawdzenie