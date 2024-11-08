FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

RUN apt-get update && apt-get install -y openjdk-17-jre openjdk-17-jdk wget && \
    wget https://github.com/allure-framework/allure2/releases/download/2.26.0/allure-2.26.0.tgz && \
    tar -zxvf allure-2.26.0.tgz -C /opt/  && \
    ln -s /opt/allure-2.26.0/bin/allure /usr/bin/allure

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
