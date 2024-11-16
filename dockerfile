FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.33.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.33.0-linux64.tar.gz

WORKDIR /app

COPY main.py test_api.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py && pytest test_api.py --html=report.html && python -m webbrowser -t report.html
