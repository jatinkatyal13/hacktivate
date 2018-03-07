from paralleldots import keywords, set_api_key, emotion, sentiment
import mch_text
from pprint import pprint
set_api_key("JlTOVs21AbroIRDXPhCOatIpjTEyQAedp8y3pKQOYVE")

def get_vects(text):
    print(str(text))

    # keywords_vect = [ k['keyword'] for k in keywords(text)['keywords'] ]
    # emotion_vect = [ (key, value) for key, value in emotion(text)['probabilities'].items() ]
    # sentiment_vect = sentiment(text)
    # del sentiment_vect['usage']
    # return [keywords_vect, emotion_vect, sentiment_vect]

    return [{"keywords": mch_text.subs(text)}, emotion(text), sentiment(text)]

if __name__ == "__main__" :
    text = str("text")
    a=get_vects(text)
    print((a))
