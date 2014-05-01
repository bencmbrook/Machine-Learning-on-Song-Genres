import network
import node_edge
from Data_Reader import *

def binaryNumbersTest():
    n_network = network.Network()
    inputNodes = [node_edge.Input_Node(i) for i in range(3)]
    hiddenNodes = [node_edge.Node() for i in range(3)]
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
    #n_network.Train(labeledExamples, 0.1, maxIterations=5000)

    # comment these two parts out and uncomment the top to get it working
    data = get_songs()
    data_list = get_data(data)
    truth_list = get_truth(data)

    def new_data (data):
      tune_list = []
      tune_data = get_data(data)
      tune_truth = get_truth(data)

      for i in range(0,len(data)): 
          usable = (tune_data[i], tune_truth[i])
          tune_truth.append(usable)

      return tune_list

    n_network.Train(new_data(data), 0.2, maxIterations=5000)

    # test for consistency
    for number, isEven in labeledExamples:
        print "Error for %r is %0.4f. Output was:%0.4f" % (number, isEven - n_network.Evaluate(number), n_network.Evaluate(number))

binaryNumbersTest()