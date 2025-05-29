# PixelLock

Esteganografia com Imagens Digitais via Web – Codificação e Decodificação de Mensagens Secretas.

[Veja o site em produção!](https://pedrokourly.pythonanywhere.com/)

## Sobre o Projeto
O PixelLock é uma aplicação web que permite esconder mensagens secretas dentro de imagens PNG utilizando técnicas de esteganografia. Com uma interface simples e intuitiva, você pode criptografar e descriptografar mensagens de forma rápida e segura, diretamente do navegador.

### Funcionalidades
- **Criptografia:** Oculte textos em imagens PNG de forma imperceptível.
- **Descriptografia:** Extraia mensagens secretas de imagens previamente criptografadas.
- **Interface Responsiva:** Compatível com dispositivos móveis e desktops.

## Como Usar
1. **Acesse o site:** [https://pedrokourly.pythonanywhere.com/](https://pedrokourly.pythonanywhere.com/)
2. **Criptografar:**
   - Vá em "Upload".
   - Envie uma imagem PNG e digite sua mensagem secreta.
   - Baixe a imagem criptografada.
3. **Descriptografar:**
   - Vá em "Revelar".
   - Envie a imagem criptografada.
   - Veja a mensagem oculta revelada na tela.

## Tecnologias Utilizadas
- Python 3
- Flask
- Pillow (PIL)
- HTML5, CSS3, Bootstrap 5
- Docker e Docker Compose

## Como rodar localmente
1. Clone o repositório:
   ```sh
   git clone https://github.com/pedrokourly/pixellock.git
   cd pixellock
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```sh
   python pixellock.py
   ```
4. Acesse `http://localhost:5000` no navegador.

### Usando Docker
1. Build e execute com Docker Compose:
   ```sh
   docker-compose up --build
   ```
2. Acesse `http://localhost:5000`.

## Licença
Este projeto está sob a licença MIT.

---
Desenvolvido por [Pedro Kourly](https://www.github.com/pedrokourly) para a disciplina de Computação Gráfica.
