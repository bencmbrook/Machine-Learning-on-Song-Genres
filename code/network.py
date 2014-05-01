# file containing the definition of network using classes in node_edge.py
from node_edge import *


class Network:
    def __init__(self):
        self.inputNodes = []
        self.hiddenNodes = []
        self.outputNodes = []
        
    def Evaluate(self, input):
        for i in range(0, len(outputNodes)):
            output[i] = self.outputNodes[i].Evaluate(input) 
        return output

    def PropagateError(self, truth):
        for node in self.inputNodes:
            node.EvalError(truth)
            
    def UpdateWeights(self, learnRate):
        for node in self.inputNodes: 
            node.Learn(learnRate)
            
    def Train(self, trainSet, learnRate, maxIterations):
        while maxIterations > 0:
            for ex,label in trainSet:
                output = self.Evaluate(ex)
                self.PropagateError(label)
                self.UpdateWeights(learnRate)
                maxIterations -= 1
    
    # adds an edge
    def AddEdge(self, origin, terminal):
        Edge.__init__(origin, terminal)
        
    # adds nodes. layer corresponds to the type of node: 1 for input, 2 for hidden and 3 for output  
    def AddNode(self, layer, index):
        
        # adding an input node
        if layer == 1:
            Input_Node.__init__(index)
        
        # adding a hidden node, with edges to all input and output nodes
        if layer == 2:
            Node.__init__()
            for inn in inputNodes:
                Edge.__init__(inn, self)
            for outn in outputNodes:
                Edge.__init__(self, outn)
        
        # adding an output node
        if layer == 3:
            Output_Node.__init__(index)