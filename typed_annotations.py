# Here we will go through typed annotations that are really helpful in python as well as langchain and langgraph

# first one is TypedDict

from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

movie_list = []
movie_list.append(Movie(title="The Matrix", year=1999))
movie_list.append(Movie(title="The Matrix Revolutions", year=2003))
print(movie_list)   



# second one is union 

from typing import Union

def square(x: Union[int, float]) -> Union[int, float]:
    return x * x

print(square(2))
print(square(2.0))


# third one is Optional

from typing import Optional

def say_hello(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello"
    else:
        return f"Hello {name}"

print(say_hello())
print(say_hello("John"))


# fourth one is Literal

from typing import Literal

def add(x: float, y: float, operation: Literal["add", "subtract", "multiply", "divide"]) -> float:
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y
    else:
        raise ValueError(f"Invalid operation: {operation}")

print(add(1.0, 2.0, "add"))
print(add(1.0, 2.0, "subtract"))
print(add(1.0, 2.0, "multiply"))
print(add(1.0, 2.0, "divide"))


# fifth one is lambda

sq = lambda x: x * x
print(sq(2))

nums = [1,2,3,4]

print(list(map(lambda x: x * x, nums)))