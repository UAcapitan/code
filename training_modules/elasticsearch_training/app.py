from elasticsearch import Elasticsearch

client = Elasticsearch("http://localhost:3000")

client.info()