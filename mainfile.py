import re
from search_module import perform_wiki_search
from call_module import make_call
from timer_module import set_timer
from tts_module import speak
from voice_module import get_voice_command

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

if __name__ == "__main__":
    main()
