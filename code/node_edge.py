from Data_Reader import get_songs
songs = get_songs()

class Node
    def __init__(self):
        self.EdgesIn = []
        self.EdgesOut = []
        self.LastOutputs = []
        self.LastInput = []
        self.Error = None
         
    def Evaluate(self, input):
        
        #store the outputs of each edge in an array
        for i, e in enumerate(self.EdgesIn):
            self.LastInput[i] = (e.in.Evaluate(input) * e.weight)
        
        #sum the elements of the input array
        output = sum(self.LastInput)
        
        #store the value to be outputted in the output array
        self.LastOutputs.append(output)    
        return sum
    
    def EvalError(self, truth):
        
        #if for some reason we haven't learned from our last error
        if self.Error != None
            return self.Error
        
        #if current node is an output node calculate error and return it
        else if self.EdgesOut == []
            self.Error = truth - self.LastOutputs[0]
            return self.Error
        
        #else sum errors of output edges and eventually return error
        else
            for e in self.EdgesOut:
                self.Error += (e.weight * e.out.EvalError(truth))
                
            return self.Error
        
    def Learn(self, LearnRate):
        if not_(self.LastOutputs = [] or self.Error = None or self.LastInput = None)
            for i, e in enumerate(self.EdgesIn):
                e.weight += (LearnRate * self.LastOutputs[0] * (1 - self.LastOutputs[0]) *
                             self.Error * self.LastInput[i]
            
            self.Error = None
            self.LastInput = None
        
class Input_Node(Node): 
    def __init__(self, index):
        Node.__init__(self)
        
        #add index of the input to be assigned to this node
        self.index = index; 
        
    def Evaluate(self, input):
        #should just return the correct value identified by index from the input
        output = input[self.index]
        self.LastOutputs.append(output)
        return output

class Edge
    def __init__(self, in, out)
        self.weight = random.uniform(0,1)
        self.in = in
        self.out = out
        
        #add self to input and output nodes
        in.EdgesOut.append(self)
        out.EdgesIn.append(self)

        
        