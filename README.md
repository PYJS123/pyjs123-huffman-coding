# pyjs123-huffman-coding
Some python code I made which can create a Huffman tree and which can compress and decompress text using Huffman coding.

## Explaining the purpose of each file
### mergesort.py
This file has a merge sort algorithm.

I made this file because during the Huffman coding algorithm, when merging nodes while creating the Huffman tree, nodes must always be ordered based on frequency. I didn't want to just use another default Python function (i.e., ```list.sort()```), so I decided I'd code an algorithm using merge sort instead, since it's one of the most efficient sorting algorithms out there and also to get some practice in.

There are two functions in the file- the actual ```mergesort``` function, which uses recursion, and the ```merge2``` function. The latter is used in the ```mergesort``` function when merging sub lists.

### nodeclasses.py
This file contains classes for nodes used in the Huffman tree.

In Huffman trees, there are two types of nodes- leaf nodes and parent nodes. Leaf nodes represent a character and, in this file, the ```Leaf``` class has two attributes- the character and frequency. Parent nodes are the result of two other nodes, which could each be parent or leaf nodes, becoming children of the same node. In this file, the ```Parent``` class has three attributes- the combined frequency of its children, the node's left child and its right child.

Both classes also contain code for printing them out (the ```__str__()``` method) which took an annoying amount of time to make and is really convoluted but it works.

### main.py
Finally, we have arrived at the main attraction- the code for the actual compression and decompression of a string using Huffman coding.

The file imports both previously mentioned files and contains 4 functions.

First is the ```huffmantree``` function which creates the tree. Then is the ```treelog``` function, which takes the resulting Huffman tree as a parameter and returns a dictionary with characters and their corresponding codes which can be used to compress text. This also uses recursion (you can tell I like recursion). The ```huffmancode``` function takes a string as a parameter, uses the ```huffmantree``` and ```treelog``` functions and returns the compressed text and the Huffman tree. Finally, the creatively named ```huffmandecode``` function takes the compressed text and Huffman tree as parameters and returns the decoded string.

I can now move on with my life.
