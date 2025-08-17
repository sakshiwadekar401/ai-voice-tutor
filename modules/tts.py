import pyttsx3

def speak_text(text, output_file="output.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file
