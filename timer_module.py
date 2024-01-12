version = "1.0"
creator = "Fox2099"
date = "10/01/2024"

from tts_module import speak
import time
import subprocess

def set_timer(duration_seconds):
    print(f"Criando cronômetro para {duration_seconds} segundos...")
    speak(f"Criando cronômetro para {duration_seconds} segundos...")
    time.sleep(duration_seconds)
    print("Timer complete!")

    # Optionally, trigger a notification to alert the user (requires additional steps)
    # For simplicity, we use a toast notification, but it might not work on all devices
    try:
        subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.TIME_SET"])
    except Exception as e:
        print(f"Error triggering notification: {e}")
