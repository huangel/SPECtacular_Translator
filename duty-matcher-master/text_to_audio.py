import pyaudio
import wave
from firebase import firebase
from google.cloud import firestore
from google.cloud import translate
import json
import sys

firebase = firebase.FirebaseApplication('https://translation-bf31b.firebaseio.com', None)
# lang = sys.argv[2]
# other_username = str(sys.argv[3])
# global lang
lang = ""

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(input_text, voice, audio_config)
    # The response's audio_content is binary.
    with open('output.wav', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

    wf = wave.open('output.wav', 'rb')
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    CHUNK = 1024
    # read data
    data = wf.readframes(CHUNK)
    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    # close PyAudio (5)
    p.terminate()
    # return response.audio_content

translate_client = translate.Client()

def translate_to_brailles(text):
    """
    input: a string of sentence 
    output: a string of brailles pattern 
    """
    ascii_string = 'abcdefghijklmnopqrstuvwxyz '
    braille_string = '⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽ '
    transtab = str.maketrans(ascii_string, braille_string)
    #convert to english
    translation = translate_client.translate(text, target_language='en')['translatedText']
    #convert to braille
    return translation.lower().translate(transtab)

db = firestore.Client()

def on_snapshot(query_snapshot, b, c):
    for doc in query_snapshot:
        # if doc.id == other_username:
        cur_indices = set(doc.to_dict().keys())
        try:
            cur_indices.remove('lang')
            max_index = max(cur_indices)
            #if output lang is braille
            if lang == "braille":
                a = translate_to_brailles(doc.to_dict()[max_index])
                print(a)
            else:
                a = synthesize_text(doc.to_dict()[max_index])
        except:
            pass
            
def main(my_username, my_lang, other_username, other_lang):
    query_ref = db.collection(u'translation').document(other_username)
    global lang
    lang = my_lang
    query_watch = query_ref.on_snapshot(on_snapshot)
    # my_dict = {el.id: el.to_dict() for el in doc}
    return
    # input()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])