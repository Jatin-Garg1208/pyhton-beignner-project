import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip(r"C:\Users\gargj\OneDrive\Desktop\SIH NEW\quiz maker\Bolna.mp4") #specify the correct file path to your video file 
clip.audio.write_audiofile(r"Bolna.wav") #this the name of the coverted audio file

r = sr.Recognizer()
audio =sr.AudioFile(r"C:\Users\gargj\OneDrive\Desktop\SIH NEW\quiz maker\Bolna.wav") # give the audio file name here
with audio as source:
    audio_file = r.record(source)
result = r.recognize_google(audio_file)
print(result)