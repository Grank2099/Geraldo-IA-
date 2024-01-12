version = "1.0"
creator = "Fox2099"
date = "10/01/2024"

from voice_module import get_voice_command
import time
import wikipedia as wiki
from tts_module import speak
wiki.set_lang("pt")

def perform_wiki_search(query):
    cont_list = (wiki.search(query))
    page = (cont_list[0])
    print (page)
    print (wiki.summary(page, sentences=4))
    speak (wiki.summary(page, sentences=4))
    time.sleep(1)
    speak ("Esse foi o resumo, gostaria de saber mais?")
    #while True:
        #full_command = get_voice_command(trigger_word='sim', language='pt-BR')
        
        
    
    
    