from langgraph.graph import StateGraph, START, END
from typing import TypedDict 


class AgentState(TypedDict):
    number1: int
    number2: int
    operation1: str
    number3: int
    number4: int
    operation2: str
    finalNumber1: int
    finalNumber2: int

def adder_node(state:AgentState) -> AgentState:
    """ this is addition node """

    state['finalNumber1'] = state['number1'] + state['number2']
    return state

def subber_node(state:AgentState) -> AgentState:
    """ this is subtraction node """

    state['finalNumber1'] = state['number1'] - state['number2']
    return state

def adder2_node(state:AgentState) -> AgentState:
    """ this is 2nd addition node """

    state['finalNumber2'] = state['number3'] + state['number4']
    return state

def subber2_node(state:AgentState) -> AgentState:
    """ this is 2nd subtraction node """

    state['finalNumber2'] = state['number3'] - state['number4']
    return state
    
def router1(state:AgentState) -> AgentState:
    if state['operation1'] == '+':
        return "addition_operation"
    else:
        return "subtraction_operation"

def router2(state:AgentState) -> AgentState:
    if state['operation2'] == '+':
        return "addition_operation2"
    else:
        return "subtraction_operation2"


graph = StateGraph(AgentState)

graph.add_node("first_node", adder_node)
graph.add_node("second_node", subber_node)
graph.add_node("third_node", adder2_node)
graph.add_node("fourth_node", subber2_node)

graph.add_node("router1", lambda state:state)
graph.add_node("router2", lambda state:state)


graph.add_edge(START, "router1")
graph.add_conditional_edges(
    "router1",
    router1,
    {
        "addition_operation": "first_node",
        "subtraction_operation": "second_node"
    }
)
graph.add_edge("first_node", "router2")
graph.add_edge("second_node", "router2")

graph.add_conditional_edges(
    "router2",
    router2,
    {
        "addition_operation2": "third_node",
        "subtraction_operation2": "fourth_node"
    }
)

graph.add_edge("third_node", END)
graph.add_edge("fourth_node", END)   

app = graph.compile()

initial_state = AgentState(
    number1 = 1,
    number2 = 2,
    operation1 = "+",
    number3 = 3,
    number4 = 4,
    operation2 = "+",
)

result = app.invoke(initial_state)

print(result)