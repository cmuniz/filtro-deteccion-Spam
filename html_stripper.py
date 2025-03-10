from html.parser import HTMLParser

class HTMLStripper(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.data = []        # Atributo que almacena los datos
        
    def handle_data(self, data):
        self.data.append(data)
