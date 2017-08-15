# Online Relationship Learning and Prediction

__Overview__

A system is a network of nodes and relations that adapt to local activity in order to maximize the efficiency of the system. Information passes through a set of input nodes and propagates throughout the network, traveling from node-to-node over relations which connect them to one another.

__Nodes__

A node receives inputs from various relations and produces a single output. When a set of inputs is received, the total sum is compared to a threshold value in order to determine the firing state of the node. Overtime the threshold adapts to fit the typical value of the sum.

__Relations__

A relation connects an initial node to a final node, allowing information to pass between them. When the initial node and final node fire in order, the elapsed time between them is compared to a delay value in order to determine the prediction performance of the relation. Overtime the delay value adapts to fit the typical value of the elapsed time.
When the initial node fires and the elapsed time is equal to the delay value, a weighted output is sent to the final node as its input. Overtime the weight value adapts to to fit the typical value of the prediction performance.

