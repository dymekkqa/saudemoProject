FROM python:3.12.0a4-alpine3.17

# Установим все нужные пакеты одним RUN
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    tzdata \
    openjdk11-jre \
    curl \
    tar \
    bash \
    wget

# Установим Allure CLI (последнюю стабильную 2.25.0)
RUN curl -o allure-2.25.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.25.0/allure-commandline-2.25.0.tgz && \
    tar -zxvf allure-2.25.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/bin/allure && \
    rm allure-2.25.0.tgz

# Рабочая директория внутри контейнера
WORKDIR /usr/workspace

# Сначала копируем только requirements.txt (для кеширования слоёв)
COPY ./requirements.txt .

# Ставим Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Установка pytest, если вдруг нет в requirements
RUN pip install --no-cache-dir pytest

# Копируем всё остальное приложение
COPY . .

# Стандартная команда (если понадобится)
CMD ["pytest"]
