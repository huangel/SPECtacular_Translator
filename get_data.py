from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://translation-bf31b.firebaseio.com', None)
with open('output.json') as f:
    output = json.load(f)

result = firebase.patch('/output', output)
print(result)