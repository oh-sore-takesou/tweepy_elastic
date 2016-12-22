from elasticsearch import Elasticsearch

class ElasticSearchHandler:
    def __init__(self):
        self.es = Elasticsearch('elasticsearch')

    def create_index(self, i_name):
        self.es.indices.create(index=i_name)

    def add_doc(self, i_name, data):
        self.es.index(index=i_name, doc_type='test', body=data)
