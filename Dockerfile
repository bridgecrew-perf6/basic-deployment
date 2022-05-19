FROM python:3.8.10-slim-buster
ARG port=8501
ENV PORT = $port

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE ${port}
ENTRYPOINT ["streamlit", "run"]
CMD --server.port $PORT test_app.py