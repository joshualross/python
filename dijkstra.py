"""A simple dijkstra implementation."""

class Edge(object):

    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __repr__(self):
        return "<Edge from:{} to:{} weight:{}>".format(
            self.from_node.name,
            self.to_node.name,
            self.weight,
        )

class Node(object):

    def __init__(self, name):
        self.name = name
        self.edges = []

    def __repr__(self):
        return "<Node {} edges:{}>".format(
            self.name,
            self.edges,
        )


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes

    def __repr__(self):
        repr = "<Graph node edges : "
        for name, node in self.nodes.iteritems():
            for edge in node.edges:
                repr += "({} - {} - {})".format(
                    edge.from_node.name,
                    edge.weight,
                    edge.to_node.name,
                )
        return repr + ">"

    def add_edge(self, edge):
        self.nodes[edge.from_node.name].edges.append(edge)
        self.nodes[edge.to_node.name].edges.append(edge)


class Dijkstras(object):

    def __init__(self, graph):
        self.graph = graph

    def shortest(self, from_node, to_node):
        """Calculate the shortest path between the nodes in terms of cost.

        from A to D:
        ------------
        A is 0
        path to B is 5
        so B is 5

        A is 0
        path to C is 10
        so C is 10

        move to B

        B is currently 5
        path to D is 2
        so D is 7

        go back and move to C

        C is currently 10
        path to D is 3
        so D is the lesser of A-B-D(7) and A-C-D(13)


        :param Node from_node:
        :param Node to_node:
        """
        print "Shortest path from {} to {}".format(from_node.name, to_node.name)
        current = from_node
        solution = {current.name: 0}
        visited = []
        if from_node.name == to_node.name:
            return "No route necessary"

        while current:
            if current.name == to_node.name:
                return "Solution {}".format(solution.get(to_node.name))

            for edge in current.edges:
                # look at routes from this node
                if edge.from_node.name != current.name:
                    continue
                weight = (solution.get(edge.from_node.name) or 0) + edge.weight
                if not solution.get(edge.to_node.name):
                    solution.update({edge.to_node.name: weight})
                elif solution.get(edge.to_node.name) > weight:
                    solution.update({edge.to_node.name: weight})

            # find the lowest weight, go to that node next
            lowest = None
            next_node = None
            for node_name, weight in solution.iteritems():
                if node_name in visited:
                    continue
                if lowest is None or weight < lowest:
                    lowest = weight
                    next_node = self.graph.nodes.get(node_name)
            visited.append(current.name)
            current = next_node
        return "No solution"

nodes = {
    'A': Node('A'),
    'B': Node('B'),
    'C': Node('C'),
    'D': Node('D'),
    'E': Node('E'),
    'F': Node('F'),
    'G': Node('G'),
    'H': Node('H'),
}


graph = Graph(nodes)
graph.add_edge(Edge(nodes['A'], nodes['B'], 5))
graph.add_edge(Edge(nodes['A'], nodes['C'], 10))
graph.add_edge(Edge(nodes['B'], nodes['C'], 2))
graph.add_edge(Edge(nodes['B'], nodes['D'], 3))
graph.add_edge(Edge(nodes['C'], nodes['E'], 4))
graph.add_edge(Edge(nodes['D'], nodes['E'], 6))
graph.add_edge(Edge(nodes['D'], nodes['F'], 8))
graph.add_edge(Edge(nodes['E'], nodes['F'], 1))
graph.add_edge(Edge(nodes['F'], nodes['G'], 10))
# no edge for H

dijkstras = Dijkstras(graph)
print dijkstras.shortest(nodes['A'], nodes['A'])  # No route necessary
print dijkstras.shortest(nodes['A'], nodes['G'])  # A -> B -> C -> E -> F -> G = 22
print dijkstras.shortest(nodes['C'], nodes['F'])  # C -> E -> F = 5
print dijkstras.shortest(nodes['C'], nodes['A'])  # No solution
print dijkstras.shortest(nodes['D'], nodes['G'])  # D -> E -> F -> G = 17
print dijkstras.shortest(nodes['A'], nodes['H'])  # No solution

