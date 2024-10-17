FROM python:3-alpine

RUN apk add --no-cache git redis
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Adriano-Martinez.git

WORKDIR /ajedrez-2024-Adriano-Martinez

RUN pip install -r requirements.txt

# Iniciar Redis en segundo plano y luego ejecutar tu aplicación
CMD ["sh", "-c", "redis-server --daemonize yes && coverage run -m unittest && coverage report -m && python main.py"]

# sudo docker build -t ajedrez-2024-adriano-martinez . --no-cache
# sudo docker run ajedrez-2024-adriano-martinez