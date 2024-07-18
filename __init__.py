import os
import sys
from utils.text_summarization import summarize_pdf, generate_knowledge_graph
from utils.knowledge_graph import GraphMaker, Ontology, Document
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the utils module
utils_dir = os.path.join(current_dir, 'utils')

# Add the utils directory to the system path
sys.path.append(utils_dir)

# Add the graph_maker directory to the system path
sys.path.append('/c/Users/akhil/downloads/graph_maker/graph_maker')


__all__ = [
    'summarize_pdf',
    'generate_knowledge_graph',
    "GraphMaker",
    'Ontology',
    'Document'
]
