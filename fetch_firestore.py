from google.cloud import firestore

db = firestore.Client()
query_ref = db.collection(u'users')
cur_dic = {}

def bcd(query_snapshot, b, c):
	# query_snapshot[u'ada']
	# print(doc.to_dict())
	# cur_dic = {}
	for doc in query_snapshot:
		if doc.id == 'alovelace':
			cur_indices = set(doc.to_dict().keys())
			cur_indices.remove('lang')
			max_index = max(cur_indices)
			print(doc.to_dict()[max_index])
			# print(cur_dic.keys())
			# print(doc.to_dict().keys())
			# diff = set(doc.to_dict().keys()) - set(cur_dic.keys())
			# print(diff)
			# cur_dic = doc.to_dict()
		# print(doc.id)
		# print(doc.to_dict())
	#print(b)
	#print(c)
  #for doc in query_snapshot.documents:
  #  print(u'{} => {}'.format(doc.id, doc.to_dict()))

query_watch = query_ref.on_snapshot(bcd)

# Create a callback on_snapshot function to capture changes
# def on_snapshot(doc_snapshot, changes, read_time):
# 	for change in changes:
# 		if change.type.name == 'ADDED':
# 			print(u'New city: {}'.format(change.document.id))
# 		elif change.type.name == 'MODIFIED':
# 			print(u'Modified city: {}'.format(change.document.id))
# 		elif change.type.name == 'REMOVED':
# 			print(u'Removed city: {}'.format(change.document.id))
# 	# for doc in doc_snapshot:
# 	#     print(u'Received document snapshot: {}'.format(doc.id))

# doc_ref = db.collection(u'users').document(u'alovelace')

# # Watch the document
# doc_watch = doc_ref.on_snapshot(on_snapshot)
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