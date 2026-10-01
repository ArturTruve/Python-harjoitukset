inventaario = []

def mitä_lisätään():
    esine = input("Lisää esine tai jätä tyhjäksi: ")
    while esine.lower() != "":
        inventaario.append(esine)
        esine = input("Seuraava esine, tai jätä tyhjäksi: ")
    return

def inventaarion_sisältö():
    for item in inventaario:
        print(f"- {item}")
    return