# import re
# from search_module import perform_wiki_search
# from call_module import make_call
# from timer_module import set_timer
# from tts_module import speak
# from voice_module import get_voice_command
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFloatingActionButton
# from  kivymd.uix.textfield import MDTextField
# from kivy.lang import Builder
# from kivymd.uix.button import MDRectangleFlatButton
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.label import MDLabel, MDIcon

# __version__ = "1.0"


# class GUI(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Green"
#         self.theme_cls.primary_hue = "A700"
#         self.theme_cls.theme_style="Dark"
#         label = MDLabel(text ="GeraldoAI", halign = 'center', theme_text_color = 'Custom',
#                         text_color=(0/255.0, 255.0/255.0, 0/255.0),
#                         font_style="H2")
#         btn_flat = MDRectangleFlatButton(text='Start/Stop', 
#                                 pos_hint={'center_x':0.5, 'center_y':0.4})
#         screen = Screen()
#         screen.add_widget(label)
#         screen.add_widget(btn_flat)
#         return screen
    

# def main():
    
    # speak("Olá! Iniciando sistema.")

    # while True:
    #     full_command = get_voice_command(trigger_word='geraldo', language='pt-BR')

    #     if full_command:
    #         if "pesquisa por" in full_command:
    #             # Extract search query from the command
    #             search_query = full_command.split("pesquisa por", 1)[1].strip()
    #             perform_wiki_search(search_query)
                
    #         elif "procura por" in full_command:
    #             # Extract search query from the command
    #             search_query = full_command.split("procura por", 1)[1].strip()
    #             perform_wiki_search(search_query)

    #         elif "liga pra" in full_command:
    #             # Extract contact name from the command
    #             contact_name = full_command.split("liga pra", 1)[1].strip()
    #             make_call(contact_name)
                
    #         elif "liga pro" in full_command:
    #             # Extract contact name from the command
    #             contact_name = full_command.split("liga pro", 1)[1].strip()
    #             make_call(contact_name)

    #         elif "marca" in full_command:
    #             # Extract timer duration from the command
    #             if "segundos" in full_command:
    #                 timer_norm = (re.findall(r'\d+', full_command))
    #                 timer_duration = int(timer_norm[0])
    #                 set_timer(timer_duration)
                    
    #             elif "minutos" in full_command:
    #                 timer_norm = (re.findall(r'\d+', full_command))
    #                 timer_to_convert = int(timer_norm[0])
    #                 timer_duration = 60*(timer_to_convert)
    #                 set_timer(timer_duration)
                    
    #             elif "horas" in full_command:
    #                 timer_norm = (re.findall(r'\d+', full_command))
    #                 timer_to_convert = int(timer_norm[0])
    #                 timer_duration = 3600*(timer_to_convert)
    #                 set_timer(timer_duration)
                    
    #         elif full_command == "sair":
    #             speak("Goodbye!")
    #             break
            

    #         else:
    #             speak("Desculpe, não entendi o comando, por favor tente novamente.")
    
# GUI().run()
    
    
    


from search_module import perform_wiki_search
from call_module import make_call
from timer_module import set_timer
from tts_module import speak
from voice_module import get_voice_command
import re

__version__ = "1.0"

def main():
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
                perform_wiki_search(search_query)

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
                speak("Goodbye!")
                break
            

            else:
                speak("Desculpe, não entendi o comando, por favor tente novamente.")
    
    
    
    
    
