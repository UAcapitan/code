FROM python:3.10.2-bullseye as base

WORKDIR /work

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

FROM base as prd

COPY . .