FROM python
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENV PORT 5000
EXPOSE $PORT
VOLUME ["/app/data"]
CMD ["python", "app.py"]