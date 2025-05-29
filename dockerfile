# Dockerfile para PixelLock
FROM python:3.13-slim

LABEL email="pedro.kourly@estudante.iftm.edu.br"
LABEL version="1.0"
LABEL description="Aplicação web para PixelLock"
LABEL maintainer="Pedro Kourly"
LABEL repository="https://github.com/pedrokourly/pixellock"

WORKDIR /pixellock

COPY . /pixellock
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "pixellock.py"]
