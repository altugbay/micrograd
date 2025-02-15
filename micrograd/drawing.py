from graphviz import Digraph

def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    nodes, edges = trace(root)
    dot = Digraph(format='svg', graph_attr={'rankdir':'LR'}) # Left to right
    for node in nodes:
        uid = str(id(node))
        dot.node(uid, label="{%s | data %.4f | grad %.4f }" % (node.label, node.data, node.grad), shape='record')
        if node._op:
            dot.node(uid + node._op, label= node._op)
            dot.edge(uid + node._op, uid)
        
    for(n1, n2) in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    dot.render('d', format='png', cleanup=True)