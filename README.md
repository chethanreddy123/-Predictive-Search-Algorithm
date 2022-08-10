# Predictive-Search-Algorithm:

# Working Demo - Streamlit:
### Prototype video:

[screen-capture (9).webm](https://user-images.githubusercontent.com/69640722/183834230-77dfd084-c937-4f39-9d1b-f0473da74c1a.webm)




### Auto-Complete-Results:
![Y1](https://user-images.githubusercontent.com/69640722/183831737-59368b6a-8edb-4104-b571-822cf81aee06.jpeg)
![Y2](https://user-images.githubusercontent.com/69640722/183831747-923f098a-fb83-41e9-ac61-932a8ad2b5dd.jpeg)


### Auto-Correct-Results

![Y4](https://user-images.githubusercontent.com/69640722/183831837-d44a5b92-7794-42a5-b570-d5b64519e88a.jpeg)
![Y3](https://user-images.githubusercontent.com/69640722/183831846-c2377404-8d0d-4e35-97f5-1bdd440c3dfd.jpeg)




## Created a predictive search algorithm with spell checks to accommodate for slight spelling mistakes. 
### Note : Pure AI math and Graph Data structure is much efficient and faster than NLP.
Trie-Tree is one of the most common ways to do autocomplete. The graph is structured such that a node is a word or a flag that means “add up the edges”, an edge is a letter of a word.

Here is an example:
![AutoComplete_Graph_short_1](https://user-images.githubusercontent.com/69640722/183827226-ab301310-d88a-4b14-aa9e-bf1d17feb1e5.svg)

### Trie Tree

As the user types each letter, the algorithm traverses through the graph, moving from node to node. At each node, all descendants of that node are displayed. For example, if the user typed bm, the descendants BMW, BMW x5, and BMW x3 are returned.
