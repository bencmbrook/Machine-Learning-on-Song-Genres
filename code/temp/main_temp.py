import network
import node_edge
import Data_Reader as reader

def binaryNumbersTest():
    n_network = network.Network()
    inputNodes = [node_edge.Input_Node(i) for i in range(6)]
    hiddenNodes = [node_edge.Node() for i in range(4)]
    outputNode = node_edge.Node()

    # weights are all randomized
    for inputNode in inputNodes:
        for node in hiddenNodes:
            node_edge.Edge(inputNode, node)

    for node in hiddenNodes:
        node_edge.Edge(node, outputNode)

    n_network.outputNodes = outputNode
    n_network.inputNodes.extend(inputNodes)

    #labeledExamples = [((0,0,0), 1),
    #                  ((0,0,1), 0),
    #                  ((0,1,0), 1),
    #                  ((0,1,1), 0),
    #                  ((1,0,0), 1),
    #                  ((1,0,1), 0),
    #                  ((1,1,0), 1),
    #                  ((1,1,1), 0)]
    # n_network.Train(labeledExamples, 0.25, maxIterations=5000)

    #comment these two parts out and uncomment the top to get it working
    data = reader.get_songs()

    def new_data (data):
      tune_truth = []

      for i in range(0,len(data)):
          data[i] = (genre, tune_data)
          usable = (tune_data, GetTruth(genre))
          tune_truth.append(usable)

      return tune_truth

    n_network.Train(new_data(data), 0.2, maxIterations=5000)

    # test for consistency
    for number, isEven in labeledExamples:
        print "Error for %r is %0.4f. Output was:%0.4f" % (number, isEven - n_network.Evaluate(number), n_network.Evaluate(number))

binaryNumbersTest()