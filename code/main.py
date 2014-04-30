from node_edge import *
from Data_Reader import *
from pyen import *

def makeNetwork(numIn, numHid, numOut):
    TestNetwerk = Network()
    inNodes = [Input_Node() for i in range (numIn)]#how many nodes we want#]
    hiddenNodes = [Node() for i in range(numHid)]#how many nodes we want#)]
    outNode = [Output_Node() for i in range(numOut)]


    for innodes in inNodes:
        for node1 in hiddenNodes:
            Edge(innodes, node)

    for node in hiddenNodes:
        for output in outNode:
            Edge(node, output)

    network.outputNode = outNodes
    network.inputNode.extend(inputNodes)

    return TestNetwerk

def Echonest_test(numHiddenNodes):
    Songs = get_song()

    network = makeNetwork(len(Songs[0].GetDate), numHiddenNodes)
    labeledExamples = [(x.GetData, x.GetTruth) for x in Songs]
    network.Train(labeledExamples, learningRate=0.25, maxIterations = 10000)

    print "Avg error : % .4f" % (sum(errors)* 1.0 / len(errors)) #edit

    with open('song.txt','a') as theFile:
        vals = tuple((x,network.evalute((Song.GetData))) for Song in get_song())
        line = "{%s},\n" % (",".join(["{%s}" % ",".join([str(n) for n in x]) for x in vals]),)
        theFile.write(line)


