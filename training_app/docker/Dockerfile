FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE $PORT
CMD ["python", "app.py"]