# System Components

## Nodes 
A node is an object that receives a set of weighted inputs and calculates a binary output (equating to whether it is active). A threshold determines the minimum value for an input to produce an output of 1. If an input is less than the threshold, an output of 0 is produced.

## Relations
A relation is an object that receives a binary input (state of a node) and calculates a weighted output. A delay determines the elapsed time following an input that is needed to produce a nonzero output. If the elapsed time is less than the delay, an output of 0 is produced.

## Patterns
A pattern is an object composed of nodes and relations that receives a binary set of inputs and calculates a binary output (equating to whether the pattern is active). A topology determines the propagation of signals between the initial set of inputs and the final output, based on the relations between nodes.
Patterns may be composed of sub-patterns, rather than nodes, which link to form a topology that functions like a normal pattern. Nodes and patterns have the same interface and can be used interchangeably because they’re indistinguishable in terms of external function.
