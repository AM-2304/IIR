class GraphMaker {
    constructor() {
        this.graph = {};
    }

    addNode(nodeId, nodeLabel) {
        this.graph[nodeId] = { label: nodeLabel, edges: [] };
    }

    addEdge(sourceId, targetId, edgeLabel) {
        this.graph[sourceId].edges.push({ targetId, label: edgeLabel });
    }

    drawGraph(container) {
        const graphContainer = document.createElement('div');
        graphContainer.style.width = '100%';
        graphContainer.style.height = '400px';
        graphContainer.style.border = '1px solid #ccc';
        graphContainer.style.padding = '20px';

        const graph = this.graph;
        const nodes = Object.keys(graph);
        const edges = [];

        nodes.forEach(nodeId => {
            const node = graph[nodeId];
            const nodeElement = document.createElement('div');
            nodeElement.style.width = '100px';
            nodeElement.style.height = '30px';
            nodeElement.style.background = '#f0f0f0';
            nodeElement.style.border = '1px solid #ccc';
            nodeElement.style.padding = '10px';
            nodeElement.innerText = node.label;

            graphContainer.appendChild(nodeElement);

            node.edges.forEach(edge => {
                edges.push({
                    source: nodeId,
                    target: edge.targetId,
                    label: edge.label
                });
            });
        });

        edges.forEach(edge => {
            const edgeElement = document.createElement('div');
            edgeElement.style.position = 'absolute';
            edgeElement.style.top = '50%';
            edgeElement.style.left = '50%';
            edgeElement.style.transform = 'translate(-50%, -50%)';
            edgeElement.style.width = '100px';
            edgeElement.style