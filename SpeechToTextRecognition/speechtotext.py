import speech_recognition as sr
from SpeechEmotionalRecognizer import emotionrecognizer
import pyttsx3
import cv2


class speech_to_text():
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.er = emotionrecognizer.emotion_recognizer()


    #
    def recognize_speech(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)

                print(f'Processing Emotion...')
                emotion_result = self.er.recognize_emotion(audio)
                print(f'Emotion Results:{emotion_result}')

                text = text.lower()
                return text
        except (sr.UnknownValueError,sr.WaitTimeoutError):
            self.recognizer = sr.Recognizer()
            return None

if __name__ == "__main__":
    stt = speech_to_text()
    while True:
        text = stt.recognize_speech()
        if not text:
            print(f"Unkown Value Recognized")
            continue
        print(f'Recognized:{text}')
        '''
        if text:
            print(f"Recognized:{text}")
        else:
            print(f"Unkown Value Recognized")
            
        '''
        if cv2.waitKey(1)  == ord('q'):
            print("Program Ending!")
            break

