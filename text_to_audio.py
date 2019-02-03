import pyaudio
import wave
from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://translation-bf31b.firebaseio.com', None)
lang = firebase.get("/output","lang")

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
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

def get_text(count = 0):
    print(firebase.get('/output', None))
    result = firebase.get('/output', None).keys()
    dic_keys = set()
    for key in result:
        try:
            dic_keys.add(int(key))
        except:
            pass
    min_key = min(dic_keys)
    result = firebase.get('/output', min_key)
    firebase.delete('/output', min_key)

    while True:
        yield result
        result = firebase.get('/output', None).keys()
        dic_keys = set()
        for key in result:
            try:
                dic_keys.add(int(key))
            except:
                pass
        min_key = min(dic_keys)
        result = firebase.get('/output', min_key)
        firebase.delete('/output', min_key)


    # while result != None:
    #     result = firebase.get('/output', count)
    #     count += 1
    #     yield result

    # result = firebase.get('/output', count)
    # return result


if __name__ == '__main__':
    for i in get_text():
        synthesize_text(i)