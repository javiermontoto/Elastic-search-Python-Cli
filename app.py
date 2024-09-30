from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200",  # Elasticsearch endpoint
)

# print(client.info())
print(client.search())