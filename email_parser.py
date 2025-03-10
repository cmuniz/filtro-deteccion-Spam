import email
import re
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk import PorterStemmer
from nltk.corpus import stopwords
from html_stripper import HTMLStripper

class EmailParser:

    def __init__(self):
        nltk.download('punkt_tab')
        nltk.download('stopwords')
    
    def parse(self, correo):
        # Obtenemos el cuerpo del correo electronico
        pcorreo = " ".join(self.get_body(correo))
        # Eliminamos los tags HTML
        pcorreo = self.strip_tags(pcorreo)
        # Eliminamos las urls
        pcorreo = self.remove_urls(pcorreo)
        # Transformamos el texto en tokens
        pcorreo = word_tokenize(pcorreo)
        # Eliminamos stopwords
        # Eliminamos puntuation
        # Hacemos stemming
        pcorreo = self.clean_text(pcorreo)
        return " ".join(pcorreo)      
        
    def get_body(self, correo):
        # Definicion una funcion interna que procese el cuerpo
        pcorreo = email.message_from_string(correo)
        return self._parse_body(pcorreo.get_payload())
    
    def _parse_body(self, payload):
        body = []
        if type(payload) is str:
            return [payload]
        elif type(payload) is list:
            for p in payload:
                body += self._parse_body(p.get_payload())
        return body      

    def strip_tags(self, correo):
        html_stripper = HTMLStripper()
        html_stripper.feed(correo)
        return ''.join(html_stripper.data)
    
    def remove_urls(self, correo):
        return re.sub(r"http\S+", "", correo)
    
    def clean_text(self, correo):
        pcorreo = []
        st = PorterStemmer()
        punct = list(punctuation) + ["\n", "\t"]
        for word in correo:
            if word not in stopwords.words('english') and word not in punct:
                # Aplicamos stemming
                pcorreo.append(st.stem(word))
        return pcorreo