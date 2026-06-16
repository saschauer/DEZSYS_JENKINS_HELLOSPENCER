FROM python:3.11-slim-buster

WORKDIR /python-flask

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN if [ ! -f count.txt ]; then echo "0" > count.txt; fi

EXPOSE 5556

CMD ["python", "src/hello.py"]