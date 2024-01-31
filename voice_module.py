import speech_recognition as sr
from tts_module import speak
import vosk
import pyaudio
import socket

def is_internet_connected_android():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False


def simplelistenon(language='pt-BR'):
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                full_command = recognizer.recognize_google(audio, language=language).lower()
                print(f"Full command received: {full_command}")
                return full_command

            except sr.UnknownValueError:
                print("Desculpe, não entendi o comando, tente novamente.")
                speak ("Desculpe, não entendi o comando, tente novamente.")
                return None

            except sr.RequestError as e:
                print(f"CNão foi possível extrair resultador da API de voz; {e}")
                return None

    try:
        full_command = recognizer.recognize_google(audio, language=language).lower()
        print(f"Full command received: {full_command}")
        return full_command

    except sr.UnknownValueError:
        print("Desculpe, não entendi o comando, tente novamente.")
        speak ("Desculpe, não entendi o comando, tente novamente.")
        return None

    except sr.RequestError as e:
        print(f"CNão foi possível extrair resultador da API de voz; {e}")
        return None
    

def simplelistenoff(language="pt-BR"):
    model = vosk.Model(r'vosk-model-small-pt-0.3')
    recognizer = vosk.KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        audio_data = stream.read(6000)
        if recognizer.AcceptWaveform(audio_data):
            full_command = recognizer.Result()
      
        

def get_voice_command_online(trigger_word='Geraldo', language='pt-BR'):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Diga: Geraldo...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            trigger = recognizer.recognize_google(audio, language=language).lower()
            if trigger == trigger_word:
                print("Palavra chave reconhecida...")
                break

        except sr.UnknownValueError:
            print("Desculpe, não entendi, tente novamente.")

        except sr.RequestError as e:
            print(f"Não foi possível extrair resultador da API de voz; {e}")
            speak(f"Não foi possível extrair resultador da API de voz; {e}")
    with sr.Microphone() as source:
        print("Esperando comando...")
        speak ("O que deseja?...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        full_command = recognizer.recognize_google(audio, language=language).lower()
        print(f"Full command received: {full_command}")
        return full_command

    except sr.UnknownValueError:
        print("Desculpe, não entendi o comando, tente novamente.")
        speak ("Desculpe, não entendi o comando, tente novamente.")
        return None

    except sr.RequestError as e:
        print(f"CNão foi possível extrair resultador da API de voz; {e}")
        return None

def get_voice_command_offline(trigger_word='Geraldo', language="pt-BR"):
    model = vosk.Model(r'vosk-model-small-pt-0.3')
    recognizer = vosk.KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    speak("Sem conexão externa, usando bibliotecas locais")
    
    print("Diga: Geraldo...")
    audio_data = stream.read(10000)
    
    while True:
        if recognizer.AcceptWaveform(audio_data):
            result = recognizer.Result()
            if trigger_word in result.lower():
                print("Palavra chave reconhecida")
                break
        
        print("Esperando comando...")
        speak("O que deseja?...")
        
        audio_data = stream.read(10000)
    
    full_command = recognizer.Result()
    print(f"Comando recebido: {full_command}")
    return full_command
