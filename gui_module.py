import threading
import time
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
import re
from search_module import perform_wiki_search, google_search
from call_module import make_call
from timer_module import set_timer
from tts_module import speak
from voice_module import get_voice_command
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton

kv_str = """
BoxLayout:
    orientation: 'vertical'
    padding: '10dp'

    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        md_bg_color: 0, 0.2, 0, 1  # Dark green background
        size_hint_y: None
        height: dp(100)  # Set the height of the toolbar

        MDLabel:
            text: "GeraldoAI"
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1  # Green text color
            halign: 'center'
            font_style: 'H4'  # Larger font size

    BoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5}

        MDFlatButton:
            id: control_button
            text: 'Start'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1  # Green text color
            on_release: app.toggle_detection()

        Label:
            id: status_label
            text: 'Voice Detection: Stopped'
            halign: 'center'
            text_size: self.width, None  # Remove the text box
"""

class GeraldoAI(MDApp):
    def build(self):
        self.shared_variable = {'detect_voice': False}
        return Builder.load_string(kv_str)

    def toggle_detection(self):
        # Toggle the state of voice detection
        self.shared_variable['detect_voice'] = not self.shared_variable['detect_voice']

        # Update GUI button text and status label
        control_button = self.root.ids.control_button
        status_label = self.root.ids.status_label
        if self.shared_variable['detect_voice']:
            control_button.text = 'Stop'
            status_label.text = 'Função principal: Rodando'
            threading.Thread(target=self.voice_command_detection_thread).start()
        else:
            control_button.text = 'Start'
            status_label.text = 'Função principal: Parada'

    def voice_command_detection_thread(self):
        while self.shared_variable['detect_voice']:
            speak("Olá! Iniciando sistema.")

            while True:
                full_command = get_voice_command(trigger_word='geraldo', language='pt-BR')

                if full_command:
                    if "pesquisa por" in full_command:
                        # Extract search query from the command
                        search_query = full_command.split("pesquisa por", 1)[1].strip()
                        perform_wiki_search(search_query)
                        
                    elif "procura por" in full_command:
                        # Extract search query from the command
                        search_query = full_command.split("procura por", 1)[1].strip()
                        google_search(search_query)

                    elif "liga pra" in full_command:
                        # Extract contact name from the command
                        contact_name = full_command.split("liga pra", 1)[1].strip()
                        make_call(contact_name)
                        
                    elif "liga pro" in full_command:
                        # Extract contact name from the command
                        contact_name = full_command.split("liga pro", 1)[1].strip()
                        make_call(contact_name)

                    elif "marca" in full_command:
                        # Extract timer duration from the command
                        if "segundos" in full_command:
                            timer_norm = (re.findall(r'\d+', full_command))
                            timer_duration = int(timer_norm[0])
                            set_timer(timer_duration)
                            
                        elif "minutos" in full_command:
                            timer_norm = (re.findall(r'\d+', full_command))
                            timer_to_convert = int(timer_norm[0])
                            timer_duration = 60*(timer_to_convert)
                            set_timer(timer_duration)
                            
                        elif "horas" in full_command:
                            timer_norm = (re.findall(r'\d+', full_command))
                            timer_to_convert = int(timer_norm[0])
                            timer_duration = 3600*(timer_to_convert)
                            set_timer(timer_duration)
                            
                    elif full_command == "sair":
                        speak("Até breve!")
                        break
                    

                    else:
                        speak("Desculpe, não entendi o comando, por favor tente novamente.")
            time.sleep(1)

if __name__ == '__main__':
    GeraldoAI().run()