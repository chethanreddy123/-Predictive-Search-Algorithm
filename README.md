# Predictive-Search-Algorithm:

# Working Demo - Streamlit:
### Prototype video:

[screen-capture (10).webm](https://user-images.githubusercontent.com/69640722/184060981-6fb23941-071f-4297-9fdf-cd4751014eb4.webm)





### Auto-Complete-Results:
![Y1](https://user-images.githubusercontent.com/69640722/183831737-59368b6a-8edb-4104-b571-822cf81aee06.jpeg)


### Auto-Correct-Results

![Y4](https://user-images.githubusercontent.com/69640722/183831837-d44a5b92-7794-42a5-b570-d5b64519e88a.jpeg)

### Comparision of NLP and AI - Model


![TY3](https://user-images.githubusercontent.com/69640722/184060664-6926158d-cc4c-4400-8941-8d4b3516ed38.jpeg)
![TY2](https://user-images.githubusercontent.com/69640722/184060539-15e78a38-de0e-4624-907a-8cc10d03018a.jpeg)
![TY1](https://user-images.githubusercontent.com/69640722/184060549-55b212eb-0e0f-456c-be07-f7bee1ed10d9.jpeg)



## Created a predictive search algorithm with spell checks to accommodate for slight spelling mistakes. 
### Note : Pure AI math and Graph Data structure is much efficient and faster than NLP.
Trie-Tree is one of the most common ways to do autocomplete. The graph is structured such that a node is a word or a flag that means “add up the edges”, an edge is a letter of a word.

Here is an example:
![AutoComplete_Graph_short_1](https://user-images.githubusercontent.com/69640722/183827226-ab301310-d88a-4b14-aa9e-bf1d17feb1e5.svg)

### Trie Tree

As the user types each letter, the algorithm traverses through the graph, moving from node to node. At each node, all descendants of that node are displayed. For example, if the user typed bm, the descendants BMW, BMW x5, and BMW x3 are returned.
