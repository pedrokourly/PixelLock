from PIL import Image
class Esteganograma:
    def __init__(self):
        pass

    # Função para converter uma string em binário
    @staticmethod
    def str_to_bin(text):
        return ''.join(format(ord(c), '08b') for c in text)

    # Função para converter binário em string
    @staticmethod
    def bin_to_str(binary):
        chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
        return ''.join([chr(int(char, 2)) for char in chars])

    # Função para esconder texto em imagem usando LSB
    @staticmethod
    def hide_text_in_image(image, secret_text):
        img = Image.open(image)
        img = img.convert('RGB')
        pixels = img.load()
        
        binary_text = Esteganograma.str_to_bin(secret_text) + '1111111111111110'  # delimitador de fim
        idx = 0

        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                if idx < len(binary_text):
                    r = (r & ~1) | int(binary_text[idx])
                    idx += 1
                if idx < len(binary_text):
                    g = (g & ~1) | int(binary_text[idx])
                    idx += 1
                if idx < len(binary_text):
                    b = (b & ~1) | int(binary_text[idx])
                    idx += 1
                pixels[x, y] = (r, g, b)
                if idx >= len(binary_text):
                    break
            if idx >= len(binary_text):
                break

        return img

    # Função para extrair texto da imagem
    @staticmethod
    def extract_text_from_image(image):
        img = Image.open(image)
        img = img.convert('RGB')
        pixels = img.load()

        binary_text = ''
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                binary_text += str(r & 1)
                binary_text += str(g & 1)
                binary_text += str(b & 1)

        # Encontrar delimitador de fim
        end_index = binary_text.find('1111111111111110')
        if end_index != -1:
            message_bits = binary_text[:end_index]
            if len(message_bits) % 8 != 0:
                return "Erro: mensagem truncada ou delimitador mal posicionado. (Mensagem não encontrada)"
            return Esteganograma.bin_to_str(message_bits)
        else:
            return "Erro: Delimitador de fim não encontrado."