import speech_recognition as sr
from tts_module import speak

def get_voice_command(trigger_word='Geraldo', language='pt-BR'):
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