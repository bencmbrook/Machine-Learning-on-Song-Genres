class Node:
    def __init__(self):
        self.EdgesIn = []
        self.EdgesOut = []
        self.LastOutputs = []
        self.Error = 0.0

         
    def Evaluate(self, input):
        sum = 0
        
        #sum the outputs of each incoming edge
        for e in self.EdgesIn
            sum += sum + (e.in.Evaluate(input) * e.weight)
         
        self.LastOutputs.append(sum)    
        return sum

    def evaluate(self, inputVector):
      self.lastInput = []
      weightedSum = 0
 
      for e in self.incomingEdges:
         theInput = e.source.evaluate(inputVector)
         self.lastInput.append(theInput)
         weightedSum += e.weight * theInput
 
      self.lastOutput = activationFunction(weightedSum)
      return self.lastOutput
    

       
            
        
class Input_Node(Node): 
    def __init__(self, index):
        Node.__init__(self)
        
        #add index of the input to be assigned to this node
        self.index = index; 

   
    def evaluate(self, inputVector):
      self.lastOutput = inputVector[self.index]
      return self.lastOutput


class Edge
    def __init__(self, in, out):
        self.weight = random.uniform(0,1)
        self.in = in
        self.out = out
        
        #add self to input and output nodes
        in.EdgesOut.append(self)
        out.EdgesIn.append(self)

class BiasNode(InputNode):
   def __init__(self):
      Node.__init__(self)
 
   def evaluate(self, inputVector):
      return 1.0

class NeuralNetwork
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
        
        