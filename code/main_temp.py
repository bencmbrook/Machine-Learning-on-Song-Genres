import network
import node_edge
from Data_Reader import *
from random import shuffle

def binaryNumbersTest(hid, learnrate, iterations):
    n_network = network.Network()
    inputNodes = [node_edge.Input_Node(i) for i in range(10)]
    hiddenNodes = [node_edge.Node() for i in range(0, hid)]
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
    
    shuffle(trainer)

    #for train in trainer:
    #    print train

    #print trainer
    n_network.Train(trainer, learnrate, maxIterations=iterations)

    # test for consistency
    return n_network
  #for trainee in trainer: #range(0, len(data)):
 #       inputs, genre = trainee
  #      print inputs
   #     print genre
    #    print n_network.Evaluate(inputs) 

def printer(net):

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
    #for train in trainer:
        #print train
    #print len(trainer)
    total = 0
    correct = 0
    for trainee in trainer: #range(0, len(data)):
        total += 1
        inputs, genre = trainee
        
        #print genre
        guess = net.Evaluate(inputs)
        
        for i in range(0, len(genre)):
            if max(genre) == (genre[i]):
                print guess
                if max(guess) == guess[i]: 
                    correct += 1
    print correct
    print total     



    

#for i in range(1, 25):
netwerk = binaryNumbersTest(10, 0.005, 20000)
 #   print i
printer(netwerk)


# x = [[i] for i in range(0, len(trainer))]
 #   shuffle(x)
#
 #   for i in range(0, len(trainer)):
  #      a = x[i]
   #     train.append(trainer[a])
#
 #   print train