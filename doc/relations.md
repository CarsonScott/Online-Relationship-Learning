# Relations

A relation is an object that associates two nodes and allows signals to propagate between them impact their states. Three variables determine the behavior of a relation (how information is transmitted), called delay, range, and weight.
- Delay is the elapsed time which is expected to occur between the first node firing and the second node firing. 
- Range is the deviation from delay which is considered accurate in terms of the expectation of elapsed time. 
- Weight is the magnitude of the signal which is transmitted from the first node to the second when it is firing.

Each variable is passed to a gaussian function as a constant. The function receives an observed elapsed-time and returns a value between one and zero, which reflects how accurately that input is reflected by the distribution, and thus how well it can be predicted. The output is a measure of performance which is used to maximize the predictive power of the distribution.
