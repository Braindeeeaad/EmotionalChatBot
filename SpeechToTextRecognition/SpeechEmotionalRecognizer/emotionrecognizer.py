import tensorflow as tf


class emotion_recognizer():
    def __init__(self):
        self.model = tf.keras.saving.load_model('VE-1.0-Feature-Extraction-Model.keras', custom_objects=None, compile=True, safe_mode=True)

    def recognize_emotion(self):
        pass
