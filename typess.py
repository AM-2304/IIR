from pydantic import BaseModel
from typing import List, Dict, Union
from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    def __init__(self, model: None):
        pass

    @abstractmethod
    def generate(self, model: None, query: str) -> str:
        "Generate and return the first choice from chat completion as string"
        pass


class Ontology(BaseModel):
    labels: List[Union[str, Dict]]
    relationships: List[str]

    def dump(self):
        if len(self.relationships) == 0:
            return self.model_dump(exclude=["relationships"])
        else:
            return self.model_dump()

class Tests(BaseModel):
    product: str
    parameter: str
    method: str 
    interval: str

class Node(BaseModel):
    name: str
    type: str

'''
class Edge(BaseModel):
    node_1: Node
    node_2: Node
    relationship: str
    metadata: dict = {}
    order: Union[int, None] = None
'''
class Edge(BaseModel):
    node_1: Node
    node_2: Node
    relationship: str
    
class Document(BaseModel):
    text: str
    metadata: dict
