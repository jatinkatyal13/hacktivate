import requests
from pprint import pprint
subscription_key="09eb38c4986e4e569caded325e0b2460"
assert subscription_key
def subs(text):
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    text_analytics_base_url = "https://southcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    language_api_url = text_analytics_base_url + "keyPhrases"
    documents = { 'documents': [
        { 'id': '1', 'text': text}
    ]}
    response  = requests.post(language_api_url, headers=headers, json=documents)
    print(response.json())
    keyword = response.json()
    #pprint(keyword)
    p=keyword.values()
    phrases = [ k for k in keyword['documents'][0]['keyPhrases'] ]
    return phrases

if __name__ == "__main__" :
    text = str("text")
    a=subs(text)
    print((a))
