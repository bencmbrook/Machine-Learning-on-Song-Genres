import network
import node_edge

def binaryNumbersTest():
    n_network = network.Network()
    inputNodes = [node_edge.Input_Node(i) for i in range(3)]
    hiddenNodes = [node_edge.Node() for i in range(3)]
    outputNodes = [node_edge.Output_Node(i) for i in range(3)]
    outputNode = node_edge.Node()

    # weights are all randomized
    for inputNode in inputNodes:
        for node in hiddenNodes:
            node_edge.Edge(inputNode, node)

    for node in hiddenNodes:
        node_edge.Edge(node, outputNode)

    n_network.outputNode = outputNode
    n_network.inputNodes.extend(inputNodes)

    labeledExamples = [((0,0,0), 1),
                      ((0,0,1), 0),
                      ((0,1,0), 1),
                      ((0,1,1), 0),
                      ((1,0,0), 1),
                      ((1,0,1), 0),
                      ((1,1,0), 1),
                      ((1,1,1), 0)]
    n_network.Train(labeledExamples, 1000, maxIterations=5000)

    # test for consistency
    for number, isEven in labeledExamples:
        if n_network.Evaluate(number) == None:
            print n_network.Evaluate(number)
        else:
            print "Error for %r is %0.4f. Output was:%0.4f" % (number, isEven - n_network.Evaluate(number), n_network.Evaluate(number))

binaryNumbersTest()