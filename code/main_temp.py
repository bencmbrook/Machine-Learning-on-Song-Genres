def binaryNumbersTest():
   network = Network()
   inputNodes = [Input_Node(i) for i in range(3)]
   hiddenNodes = [Node() for i in range(3)]
   outputNode = Node()

   # weights are all randomized
   for inputNode in inputNodes:
      for node in hiddenNodes:
         Edge(inputNode, node)

   for node in hiddenNodes:
      Edge(node, outputNode)

   network.outputNode = outputNode
   network.inputNodes.extend(inputNodes)

   labeledExamples = [((0,0,0), 1),
                      ((0,0,1), 0),
                      ((0,1,0), 1),
                      ((0,1,1), 0),
                      ((1,0,0), 1),
                      ((1,0,1), 0),
                      ((1,1,0), 1),
                      ((1,1,1), 0)]
   network.train(labeledExamples, maxIterations=5000)

   # test for consistency
   for number, isEven in labeledExamples:
      print "Error for %r is %0.4f. Output was:%0.4f" % (number, isEven - network.evaluate(number), network.evaluate(number))