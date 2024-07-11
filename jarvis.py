
from RealtimeSTT import AudioToTextRecorder
import ollama
from os import system


if __name__ == "__main__":

    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", post_speech_silence_duration=1,)
    
    hot_words = ["jarvis"]
    print("Say something...")

    while True:

        current_text = recorder.text()
        print(current_text)

        if any(hot_word in current_text.lower() for hot_word in hot_words):
            if current_text:
                print("User: " + current_text)
                recorder.stop()
                #call jarvis
                recorder.start()
                response = ollama.chat(model='llama3', messages=[
                {
                'role': 'user',
                'content': current_text,
                },
                ])
                print(response['message']['content'])
                system('say ' + response['message']['content'])
                
