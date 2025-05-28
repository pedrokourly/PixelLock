from esteganogram import Esteganograma

import PIL

if __name__ == "__main__":
    
    teste = Esteganograma()
    texto = teste.extract_text_from_image('static/processed/teste.png')

    print(texto)