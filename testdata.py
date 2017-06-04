from database import *

session = db.session()

# usuniecie istniejacych rekordow
session.query(Folder).delete()
session.query(Document).delete()
session.query(Folder_Document_Link).delete()

session.add(Folder(folder_id = -1, parent_folder_id = -1, description='dummy root'))
session.add(Folder(folder_id = 1, parent_folder_id = -1, description='sprawy wazne i powazne'))
session.add(Folder(parent_folder_id = -1, description='zabawa i relaks'))
session.add(Folder(parent_folder_id = 1, description='bardzo wazne'))

session.add(Document(document_id=1, document_name = 'kody_do_GTA_VC.txt', content='Gdy znów do murów klajstrem świeżym Przylepiać zaczną obwieszczenia, Gdy "do ludności", "do żołnierzy" Na alarm czarny druk uderzy I byle drab, i byle szczeniak W odwieczne kłamstwo ich uwierzy, Że trzeba iść i z armat walić, Mordować, grabić, truć i palić; Gdy zaczną na tysięczną modłę Ojczyznę szarpać deklinacją I łudzić kolorowym godłem, I judzić "historyczną racją", O piędzi, chwale i rubieży, O ojcach, dziadach i sztandarach, O bohaterach i ofiarach; Gdy wyjdzie biskup, pastor, rabin Pobłogosławić twój karabin, Bo mu sam Pan Bóg szepnął z nieba, Że za ojczyznę - bić się trzeba; Kiedy rozścierwi się, rozchami Wrzask liter pierwszych stron dzienników, A stado dzikich bab - kwiatami Obrzucać zacznie "żołnierzyków". - - O, przyjacielu nieuczony, Mój bliźni z tej czy innej ziemi! Wiedz, że na trwogę biją w dzwony Króle z panami brzuchatemi; Wiedz, że to bujda, granda zwykła, Gdy ci wołają: "Broń na ramię!", Że im gdzieś nafta z ziemi sikła I obrodziła dolarami; Że coś im w bankach nie sztymuje, Że gdzieś zwęszyli kasy pełne Lub upatrzyły tłuste szuje Cło jakieś grubsze na bawełnę. Rżnij karabinem w bruk ulicy! Twoja jest krew, a ich jest nafta! I od stolicy do stolicy Zawołaj broniąc swej krwawicy: "Bujać - to my, panowie szlachta!"'))
session.add(Document(document_id=2, document_name = 'tajny_plik.txt', content='tajneA common need for data binding is manipulating an element’s class list and its inline styles. Since they are both attributes, we can use v-bind to handle them: we just need to calculate a final string with our expressions. However, meddling with string concatenation is annoying and error-prone. For this reason, Vue provides special enhancements when v-bind is used with class and style. In addition to strings, the expressions can also evaluate to objects or arrays.'))

session.add(Folder_Document_Link(folder_id = 1, document_id = 1))
session.add(Folder_Document_Link(folder_id = 1, document_id = 2))

session.commit()

print(session.execute('select * from folder f left outer join folder_document_link fd on (fd.folder_id=f.folder_id) left outer join document d on (d.document_id=fd.document_id)').fetchall()) # sprawdzenie