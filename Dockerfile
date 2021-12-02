FROM python:latest
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "pytest", "./api_tests"]