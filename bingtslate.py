# -*- coding: utf-8 -*-
import requests
import json
import uuid

def translate_text(text=None, subscriptionKey=None):
  
    if not subscriptionKey:
        try:
            subscriptionKey = open('key.txt', 'r').read().strip()
        except IOError:     
            subscriptionKey = raw_input('Podaj klucz aplikacji: ')
            
    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    app_url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
    langs = '&to=en&to=pl&to=fr&to=de&to=ar'
    url = app_url + langs    
    
    body = [{'text' : text}]
    
    response = requests.post(url, headers=headers, json=body).json()

    return response
    
def print_translations(response):

    detected_lang = response[0]['detectedLanguage']['language']
    print(u'Rozpoznany język: {}'.format(detected_lang))
    for i in response[0]['translations']:
        if i['to'] != detected_lang:
            print(u'{1}: {0}'.format(i['text'], i['to']) )

if __name__ == '__main__':
    user_text = raw_input('Podaj tekst to przetłumaczenia: ')
    output = translate_text(text=user_text)
    print_translations(output)





