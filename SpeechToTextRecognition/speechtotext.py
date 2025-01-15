import speech_recognition as sr
import pyttsx3
import cv2


class speech_to_text():
    def __init__(self):
        self.recognizer = sr.Recognizer()


    #
    def recognize_speech(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recognizer.listen(source)
                print(f'Audio len:{len(audio.frame_data)}')
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                return text
        except sr.UnknownValueError:
            self.recognizer = sr.Recognizer()
            return None

if __name__ == "__main__":
    stt = speech_to_text()
    while True:
        text = stt.recognize_speech()
        if text:
            print(f"Recognized:{text}")
        else:
            print(f"Unkown Value Recognized")
        if cv2.waitKey(1)  == ord('q'):
            print("Program Ending!")
            break

