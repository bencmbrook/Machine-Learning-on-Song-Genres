class Node
    def __init__(self)
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
            
            
        
class Input_Node(Node): 
    def __init__(self, index)
        Node.__init__(self)
        
        #add index of the input to be assigned to this node
        self.index = index; 
        
    def Evaluate(self, input):
        #should just return the correct value identified by index from the input
        #output = input[self.index]
        #self.LastOutputs.append(output)
        #return output

class Edge
    def __init__(self, in, out)
        self.weight = random.uniform(0,1)
        self.in = in
        self.out = out
        
        #add self to input and output nodes
        in.EdgesOut.append(self)
        out.EdgesIn.append(self)

        
        