from flask import Flask, request, jsonify, render_template
from utils.text_summarization import generateSummary
from utils.knowledge_graph import GraphMaker, Ontology, Document
import os

app = Flask(__name__)

@app.route('/generate_summary', methods=['POST'])
def generate_summary_route():
    return generateSummary()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_input = request.files['pdf_file']
        pdf_path = os.path.join(os.path.dirname(__file__), 'temp.pdf')
        file_input.save(pdf_path)

        # Summarize the PDF
        summary, knowledge_graph, progress, remaining_time = generateSummary(file_input)

        # Generate the knowledge graph
        graph_maker = GraphMaker()
        graph_maker.from_json(knowledge_graph)

        # Return a success message if the PDF is parsed successfully
        return render_template('index.html', message='PDF parsed successfully!')
    else:
        return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)