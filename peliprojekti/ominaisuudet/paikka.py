class Paikka:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine # Esine tai None, jos paikassa ei ole esinettä.