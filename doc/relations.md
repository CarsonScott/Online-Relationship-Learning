# Relations

A relation is an object that associates two nodes, allowing communication between a start-node and an end-node through signals that impact the state of the receiving node with respect to the strength of the signal. There are three main variables dictating the behavior of a given relation: delay, range, and weight.
- Delay is the elapsed time which is expected to occur between the first node firing and the second node firing. 
- Range is the deviation from delay which is considered acceptable in terms of the expectation of elapsed time. 
- Weight is the magnitude of the signal which is transmitted from the first node to the second when it is firing.

Delay and range are passed to a gaussian function as constants. The function receives an observed elapsed-time and returns a value between one and zero, which shows how accurately that input is reflected by the distribution, and thus how well it can be predicted. The output is a measure of performance which is used to maximize the predictive power of the distribution.
