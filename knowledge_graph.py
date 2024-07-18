import json

import networkx as nx
import matplotlib.pyplot as plt
import self
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL

class GraphMaker:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, node_label):
        self.graph.add_node(node_id, label=node_label)

    def add_edge(self, source_id, target_id, edge_label):
        self.graph.add_edge(source_id, target_id, label=edge_label)

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

    def from_documents(self, docs):
        for doc in docs:
            self.add_node(doc.metadata['generated_at'], doc.text)
            for concept in doc.concepts:
                self.add_node(concept, concept)
                self.add_edge(doc.metadata['generated_at'], concept, 'has concept')
            for relation in doc.relations:
                self.add_node(relation, relation)
                self.add_edge(doc.metadata['generated_at'], relation, 'has relation')
        return self.graph

    def to_json(self):
        graph_data = {'nodes': [], 'edges': []}
        for node in self.graph.nodes:
            graph_data['nodes'].append({'id': node, 'label': self.graph.nodes[node]['label']})
        for edge in self.graph.edges:
            graph_data['edges'].append({'source': edge[0], 'target': edge[1], 'label': self.graph.edges[edge]['label']})
        return json.dumps(graph_data)

class Ontology:
    def __init__(self):
        self.graph = Graph()
        self.namespace = Namespace("http://example.com/ontology#")

    def define_classes(self):
        self.graph.add((self.namespace.Document, RDF.type, OWL.Class))
        self.graph.add((self.namespace.Concept, RDF.type, OWL.Class))
        self.graph.add((self.namespace.Relation, RDF.type, OWL.Class))

    def define_properties(self):
        self.graph.add((self.namespace.hasTitle, RDF.type, OWL.DatatypeProperty))
        self.graph.add((self.namespace.hasContent, RDF.type, OWL.DatatypeProperty))
        self.graph.add((self.namespace.hasConcept, RDF.type, OWL.ObjectProperty))
        self.graph.add((self.namespace.hasRelation, RDF.type, OWL.ObjectProperty))

    def save_ontology(self, file_path):
        self.graph.serialize(file_path, format='turtle')

class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.concepts = []
        self.relations = []

    def add_concept(self, concept):
        self.concepts.append(concept)

    def add_relation(self, relation):
        self.relations.append(relation)