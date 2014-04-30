import random
import math

def activationFunction(x):
   return 1.0 / (1.0 + math.exp(-x))

class Node:
    def __init__(self):
        self.EdgesIn = []
        self.EdgesOut = []
        self.LastInput = None
        self.LastOutputs = None
        self.Error = None
       # self.addBias()

    #def addBias(self):
     #   self.EdgesIn.append(Edge(BiasNode(),self))

    def Evaluate(self, input):
        if self.LastOutputs is not None:
            return self.LastOutputs
        self.LastInput = []
        weightsum = 0
        print "test"
        # store the outputs of each edge in an array
        for i, e in enumerate(self.EdgesIn):
            firstInput = e.inp.Evaluate(input) 
            self.LastInput.append(firstInput)
            weightsum += firstInput * e.weight
           # print i, e
        
        # sum the elements of the input array
        self.lastOutput = activationFunction(weightsum)
        # store the value to be outputted in the output array
        return self.lastOutput

#    def evaluate(self, inputVector):
#        self.lastInput = []
#        weightedSum = 0
# 
#        for e in self.incomingEdges:
#            theInput = e.source.evaluate(inputVector)
#            self.lastInput.append(theInput)
#            weightedSum += e.weight * theInput
# 
#        self.lastOutput = activationFunction(weightedSum)
#        return self.lastOutput
    
    def EvalError(self, truth):
        # if for some reason we haven't learned from our last error
        if self.Error is None:
            return self.Error
        
        # if current node is an output node calculate error and return it
        # else if self.EdgesOut == []
            # self.Error = truth - self.LastOutputs[0]
            # return self.Error
        
        # else sum errors of output edges and eventually return error
        else:
            for e in self.EdgesOut:
                self.Error += (e.weight * e.out.EvalError(truth))
                
            return self.Error
        
    def Learn(self, LearnRate):
        if self.LastOutputs is not None and self.Error is  not None and self.LastInput is not None:
            for i, e in enumerate(self.EdgesIn):
                e.weight += (LearnRate * self.LastOutputs * (1 - self.LastOutputs) * self.Error * self.LastInput[i]) 
            for edge in self.EdgesOut:
                edge.out.Learn(LearnRate)           
        
class Output_Node(Node):
    def __init__(self, index):
        Node.__init__(self)
        
        # add index of the output of this node for the creation of the single output vector
        self.index = index
        
    def EvalError(self, truth):
        self.Error = truth[self.index] - self.LastOutputs
        return self.Error
        
        
class Input_Node(Node): 
    def __init__(self, index):
        Node.__init__(self)
        
        # add index of the input to be assigned to this node
        self.index = index; 
        
    def Evaluate(self, inputvector):
        # should just return the correct value identified by index from the input
        self.LastOutput = inputvector[self.index]        
        return self.LastOutput

class Edge:
    def __init__(self, inp, out):
        self.weight = random.uniform(0,1)
        self.inp = inp
        self.out = out
        
        # add self to input and output nodes
        inp.EdgesOut.append(self)
        out.EdgesIn.append(self)

class BiasNode(Input_Node):
    def __init__(self):
        Node.__init__(self)
 
    def evaluate(self, inputVector):
        return 1.0

class NeuralNetwork:
    def __init__(self):
        self.inputNodes = []
        self.outputNode = None

    def evaluate(self, inputVector):
        return self.outputNode.evaluate(inputVector)

    def propagateError(self, label):
        for node in self.inputNodes:
            node.getError(label)
 
    def updateWeights(self, learningRate):
        for node in self.inputNodes:
            node.updateWeights(learningRate)
 
    def train(self, labeledExamples, learningRate=0.9, maxIterations=10000):
        while maxIterations > 0:
            for example, label in labeledExamples:
                output = self.evaluate(example)
                self.propagateError(label)
                self.updateWeights(learningRate)
 
                maxIterations -= 1
        
        