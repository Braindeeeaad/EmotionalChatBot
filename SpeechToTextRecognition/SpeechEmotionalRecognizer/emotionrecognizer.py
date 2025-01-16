import tensorflow as tf
from tensorflow.keras import models
import numpy as np
import librosa
from IPython.display import Audio
import warnings
import os


class emotion_recognizer():
    def __init__(self):
        self.model = models.load_model('SpeechEmotionalRecognizer/VE-1.0-Feature-Extraction-Model.keras')
        self.class_lables = ['neutral','calm','happy','sad','angry', 'fearful', 'disgust', 'suprised']

    def process_audio(self,audio):
        # Extract raw audio data
        raw_data = audio.frame_data
        sample_width = audio.sample_width

        # Determine the correct dtype based on sample width
        if sample_width == 1:
            dtype = np.uint8  # 8-bit unsigned PCM
        elif sample_width == 2:
            dtype = np.int16  # 16-bit signed PCM
        elif sample_width == 4:
            dtype = np.int32  # 32-bit signed PCM
        else:
            raise ValueError(f"Unsupported sample width: {sample_width}")

        # Convert raw data to NumPy array
        audio_array = np.frombuffer(raw_data, dtype=dtype)

        # Normalize to range [-1, 1] for librosa
        audio_array = audio_array.astype(np.float32) / np.iinfo(dtype).max
        return audio_array
    def extract_mfcc(self,audio: Audio):
        y, sr = self.process_audio(audio), audio.sample_rate
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
        mfcc = mfcc.reshape(1, 40, 1)
        return mfcc

    def recognize_emotion(self, audio: Audio):
        mfcc = self.extract_mfcc(audio)
        result = self.model.predict(mfcc)
        emotion_idx = np.argmax(result)
        predicted_emotion = self.class_lables[emotion_idx]
        return predicted_emotion
