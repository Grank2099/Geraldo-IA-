version = "1.0"
creator = "Fox2099"
date = "10/01/2024"

from voice_module import simplelisten
import time
import wikipedia as wiki
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from tts_module import speak
from listas import afirmacoes, negacoes
wiki.set_lang("pt")

def perform_wiki_search(query):
    cont_list = (wiki.search(query))
    page = (cont_list[0])
    padrao = (wiki.summary(page, sentences=4))
    print (page)
    print (padrao)
    speak (padrao)
    time.sleep(1)
    speak ("Esse foi o resumo, gostaria de saber mais?")
    full_command = simplelisten(language='pt-BR')
    if full_command in afirmacoes:
        print("Ok! Aqui está a continuação")
        speak("Ok! Aqui está a continuação")
        tudo = wiki.summary(page)
        resto = tudo.replace(padrao, "").lstrip()
        speak(resto)
    if full_command in negacoes:
        print("Ok! Voltando a função principal")
        speak("Ok! Voltando a função principal")
        
def google_search(query, num_results=1):
    search_results = list(search(query, num_results=num_results))

    if not search_results:
        print("Nenhum resultado foi encontrado.")
        return

    first_result = search_results[0]
    print(f"Primeiro resultado: {first_result}")
    speak(f"Lendo primeiro resultado {first_result}")

    try:
        page = requests.get(first_result)
        soup = BeautifulSoup(page.content, 'html.parser')
        paragraphs = soup.find_all('p')
        summary = ' '.join([paragraph.text for paragraph in paragraphs[:3]])  # Extracting the first 3 paragraphs as a summary
        print(f"Resumo: {summary}")
        speak(summary)
    except Exception as e:
        print(f"Erro ao criar resumo: {e}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    