import network
import node_edge
from Data_Reader import *

def binaryNumbersTest():
    n_network = network.Network()
    inputNodes = [node_edge.Input_Node(i) for i in range(10)]
    hiddenNodes = [node_edge.Node() for i in range(8)]
    outputNodes = [node_edge.Output_Node(i) for i in range(7)]

    # weights are all randomized
    for inputNode in inputNodes:
        for node in hiddenNodes:
            node_edge.Edge(inputNode, node)

    for node in hiddenNodes:
        for outnode in outputNodes:
            node_edge.Edge(node, outnode)

    n_network.outputNodes.extend(outputNodes)
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

    def new_data (data):
        tune_list = []
        tune_data = get_data(data)
        tune_truth = get_truth(data)

        for i in range(0,len(data)): 
            usable = (tune_data[i], tune_truth[i])
            tune_list.append(usable)

        return tune_list

    trainer = new_data(data)

    n_network.Train(trainer, 0.2, maxIterations=10)
    
    # test for consistency
    for i in range(0, len(trainer[1].tune_data)):
        print "Output was:%0.4f" % n_network.Evaluate(trainer.tune_data[i])




binaryNumbersTest()