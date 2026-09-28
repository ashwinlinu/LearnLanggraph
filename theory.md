here we are learning about state in LangGrapgh


State is a shared data structure that holds the current information or context of the entire application its like an application memory, keeping track of the variables and data that a node can access and modify as they execute 


Nodes are individual funtions or operations that perform specific task within the graph.
Each node recieves input (often current state), process it and produces an output or an updated state.


Graph in Langgraph is the overarching structure that maps different tasks are connected and executed.
It visually represents the workflow

Edges are the connections between the nodes that determine the flow of execution. They tells us which node should be exceuted next after the current one completes its task.

one more type of edge is conditional edge --->  these are specialized connections that decide the next node to execute based on specific conditions or logic is applied to the current state.

Start node or its a virtual entry point in the LangGraph, marking where the workflow begins 

End elements or Node - The end node signifies the conclusion of the workflow in LangGraph

Tools -  Tools are speacialized funtions or utilities that node can utilize to perform specific task such as fetching data from an API

ToolNode - ToolNode is a just a special kind of node whose main job is to run a tool,  it connect the tools data back on to the state

StateGraph -- its a class used to build and compile the graph structure

Runnable is standardized excecutalbe component that performs a specific task within an AI workflow

message types -- Human Message, System Message, Funtion Message, Ai Message, Tool Message.