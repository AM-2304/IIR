import os
import datetime
import json
import sys
import pymupdf
from flask import request, jsonify
from langchain_community.llms import Cohere
from utils.knowledge_graph import GraphMaker, Document, Ontology

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'langchain_community'))
import langchain_community.llms.cohere as cohere

def generateSummary():
    file_input = request.files['pdf_file']
    if not file_input:
        return jsonify({'error': 'Please select a PDF file to generate the summary.'}), 400

    summary, knowledge_graph, progress, remaining_time = summarize_pdf(file_input)

    data = {
        'summary': summary,
        'knowledge_graph': knowledge_graph.to_json(),
        'ontology': {},  # Not implemented
        'progress': progress,
        'remaining_time': remaining_time
    }

    return jsonify(data)

def summarize_pdf(pdf_file):
    example_text_list = []
    doc = pymupdf.open(pdf_file)
    for page in doc:
        text = page.get_text()
        example_text_list.append(text)

    llm = cohere.Cohere(
        model_path="/mnt/c/Users/akhil/Downloads/graph_maker/graph_maker/Meta-Llama-3-8B-Instruct-Q6_K.gguf",
        temperature=0.2,
        max_new_tokens=8192,
        context_window=8192,
        model_kwargs={"n_gpu_layers": -1},
        verbose=True,
    )

    current_time = str(datetime.datetime.now())
    docs = [Document(text=t, metadata={"summary": generate_summary(t, llm), 'generated_at': current_time}) for t in
            example_text_list]

    graph_maker = GraphMaker()
    graph = graph_maker.from_documents(docs)

    return '', graph, 0, 0

def generate_summary(text, llm):
    SYS_PROMPT = (
        "Succintly summarise the following text: \n"
        f"{text}"
        ". Respond only with the exact answer and no other comments"
    )
    try:
        summary = llm.complete(SYS_PROMPT)
    except:
        summary = ""
    finally:
        return summary

def generate_knowledge_graph(pdf_file):
    summary, knowledge_graph, progress, remaining_time = summarize_pdf(pdf_file)
    return knowledge_graph