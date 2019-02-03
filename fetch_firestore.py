from google.cloud import firestore

db = firestore.Client()
query_ref = db.collection(u'users')

def on_snapshot(query_snapshot, b, c):
	for doc in query_snapshot:
		print(doc.id)
		print(doc.to_dict())
	#print(b)
	#print(c)
  #for doc in query_snapshot.documents:
  #  print(u'{} => {}'.format(doc.id, doc.to_dict()))

query_watch = query_ref.on_snapshot(on_snapshot)

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# # Then query for documents
# users_ref = db.collection(u'users')
# docs = users_ref.get()

# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))
input()