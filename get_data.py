from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://translation-bf31b.firebaseio.com', None)
# with open('output.json') as f:
#     output = json.load(f)

result = firebase.get('/output', None).keys()

dic_keys = set()

for key in result:
	try:
		dic_keys.add(int(key))
	except:
		pass
print(dic_keys)