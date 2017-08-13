# Online Relationship-Learning and Prediction

## Relations

A relation is an object that associates two nodes, allowing communication between a start-node and an end-node through signals that impact the state of the receiving node with respect to the strength of the signal. There are three main variables dictating the behavior of a given relation: delay, range, and weight.
- Delay is the elapsed time which is expected to occur between the first node firing and the second node firing. 
- Range is the deviation from delay which is considered acceptable in terms of the expectation of elapsed time. 
- Weight is the magnitude of the signal which is transmitted from the first node to the second when it is firing.

Delay and range are passed to a gaussian function as constants. The function receives an observed elapsed-time and returns a value between one and zero, which shows how accurately that input is reflected by the distribution, and thus how well it can be predicted. The output is a measure of performance which is used to maximize the predictive power of the distribution.

## Concepts and Sequences

A sequence is a chain  of nodes linked by sequential relations. The first node in the chain sends a signal to the second node, which is delayed by some amount of time. The second node becomes active once that signal is received, and produces another signal which propagates to the third, and so on. The result is a cascade of activity traveling between nodes in a specific order. The order is determined by repeated observations of activity, where the firing patterns of the nodes tend toward a specific arrangement through time, and the temporal difference between each node and the previous tend toward a specific value. A concept is a collection of nodes linked by conceptual relations. Each node is connected to a set of other nodes nearby in space. The result is a cascade of activity traveling between nodes in a cyclic manner. The configuration is determined by repeated observations of activity, where the firing patterns of the nodes tend toward a specific arrangement over space, and the distance/angle between them tend toward specific values.

![](https://github.com/CarsonScott/Online-Relationship-Learning/blob/master/img/Patterns.PNG)

Sequences, being a product of time, require just one dimension for an accurate representation of their patterns. However, concepts exist in space and therefore cannot be represented in the same way. Both have an interval, distance and delay, which are equivalent in that they measure the difference between two things. Objects in two-dimensional space are related through measurements of distance and rotation to represent their differences in space.
