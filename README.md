# Online Relationship-Learning and Prediction

The following is an outline for an unsupervised machine-learning algorithm that predicts and adapts to input patterns in real-time. For part one of this project, see [online category learning](https://github.com/CarsonScott/Online-Category-Learning).

## Overview

A system is a network of nodes and links that adapt to local activity in order to maximize the efficiency of the system. Information passes through a set of input nodes and propagates throughout the network, traveling from node-to-node over links which connect them to one another.

A node receives inputs from various links and produces a single output. When a set of inputs is received, the total sum is compared to a threshold value in order to determine the firing state of the node. Overtime the threshold adapts to fit the typical value of the sum.

![Node](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Node.png)

A link connects an initial node to a final node, allowing information to pass between them. When the initial node and final node fire in order, the elapsed time between them is compared to a delay value in order to determine the prediction performance of the relation. Overtime the delay value adapts to fit the typical value of the elapsed time. When the initial node fires and the elapsed time is equal to the delay value, a weighted output is sent to the final node as its input. Overtime the weight value adapts to to fit the typical value of the prediction performance.

![Link](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Link.png)

## Examples 

The following graph displays the prediction error of a single relation between two nodes as it changes over time. As you can see, it falls dramatically as the system trains itself to make better predictions. Firing occurs every 10 iterations and alternates between the two. The relation between them is responsible for making predictions about when the next firing will occur. Errors reflect the difference between a predicted time that a firing will occur and the observed time that it does occur.

![Prediction Error](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Prediction%20Error.PNG)

In this second graph, a sequence of three nodes are linked in order. The first two receive the network's inputs and the third produces its output. The sequence of input patterns consists of one pattern of all 0s, one where the first node receives a 1 and the second receives a 0, and finally a pattern where the first receives a 0 and the second a 1. This sequence is passed in a loop to the network while each node is being trained. Thresholds are adapted to fit a node's total input value, referred to as its estimation, and the estimation errors reflect the difference between an estimated input value and the actual value that is received. 

![Estimation Error](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Estimation%20Error.PNG)
