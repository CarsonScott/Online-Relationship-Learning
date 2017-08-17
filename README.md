# Online Relationship-Learning and Prediction

The following is an outline for an unsupervised machine-learning algorithm that predicts and adapts to input patterns in real-time.

## Overview

A system is a network of nodes and links that adapt to local activity in order to maximize the efficiency of the system. Information passes through a set of input nodes and propagates throughout the network, traveling from node-to-node over links which connect them to one another.

![Node](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Node.png)

A node receives inputs from various links and produces a single output. When a set of inputs is received, the total sum is compared to a threshold value in order to determine the firing state of the node. Overtime the threshold adapts to fit the typical value of the sum.

![Link](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Link.png)

A link connects an initial node to a final node, allowing information to pass between them. When the initial node and final node fire in order, the elapsed time between them is compared to a delay value in order to determine the prediction performance of the relation. Overtime the delay value adapts to fit the typical value of the elapsed time. When the initial node fires and the elapsed time is equal to the delay value, a weighted output is sent to the final node as its input. Overtime the weight value adapts to to fit the typical value of the prediction performance.

## Examples

The following  (simple) example is a system of 30 nodes, with the first 5 being input nodes whose firing states are set directly by values passed to to the system. The rest of the nodes receive inputs via relations that connect it to the previous 5 nodes that come before it. For each training iteration, the system receives a set of inputs which are used to override the states of the input nodes. The sequence of inputs used here are as follows:

	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{0, 0, 0, 0, 0}
	{1, 0, 0, 0, 0}
	{1, 1, 0, 0, 0}
	{1, 1, 1, 0, 0}
	{1, 1, 1, 1, 0}
	{1, 1, 1, 0, 0}
	{1, 1, 0, 0, 0}
	{1, 0, 0, 0, 0}
  
The system recieves one of these sets (in order) at each iteration and uses it to update the nodes and links that make up its network. It is essentially training and functioning simultaneously, making it an example of an online-learning algorithm, or an algorithm that adapts in real-time. After it finishes processing the inputs, a mean prediction error is caluclated from that of every link. Below is a graph depicting this value over 10,000 iterations:
  
![Error](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Error%20rate.PNG)

As you can see, the error begins to plateau just under 1.5, meaning the the average difference between a predicted number oftime-steps between two nodes firing and the actual number is less than 2. In other words, the average expectation tends to fall within 1.5 time-steps of the actual value it is measuring. Given that each time-step is a whole number equal to its predecessor plus 1, a time-frame of less than 2 is relatively trivial, particularly in this case where we are using errors to guage the fitness ratings of links that are operating on variables with a minimum nonnegative value of 1. 

In any case, the system displays an adequate ability in converging to the spatio-temporal parameters of its inputs. Each node continuously adapts to fit a particular input magnitude (space), while each link adapts to fit a particular firing delay (time) between nodes. of course the example given above has only feedforward connections. The capabilities, as well as complexities, of a system scale with the number of recurrent links between its nodes. For that reason a simple feedforward network is an efficient way to exhibit the learning abilities of a system while avoiding the nonlinearity associated with bidirectional flow of data.
