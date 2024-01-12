import requests
from bs4 import BeautifulSoup
import pyttsx3

def search_and_speak(query):
    # Function to perform web search using DuckDuckGo search engine
    def perform_web_search(query):
        search_url = f'https://duckduckgo.com/html?q={query}'
        response = requests.get(search_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error performing web search. Status code: {response.status_code}")
            return None

    # Function to extract and speak the content of the first search result
    def speak_search_result(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        first_result = soup.find('div', class_='result__body')
        if first_result:
            result_text = first_result.get_text(strip=True)
            speak_text(result_text)
        else:
            speak_text("No search results found.")

    # Function to use pyttsx3 to speak text
    def speak_text(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Perform web search and speak the first result
    html_content = perform_web_search(query)
    if html_content:
        speak_search_result(html_content)