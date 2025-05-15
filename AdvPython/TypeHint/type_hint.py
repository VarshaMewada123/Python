

# ------------------------------------------------------------
# 🔸 1. Variable Type Hints
# ------------------------------------------------------------
# You can tell Python what type a variable is supposed to be
# This does not enforce the type at runtime, but helps in code clarity and tools like mypy.

count: int = 42              # 'count' should be an integer
name: str = "Alice"          # 'name' should be a string
pi: float = 3.14             # 'pi' should be a float

# You can also declare a variable's type without assigning a value:
config_path: str             # This is just a declaration

# ------------------------------------------------------------
# 🔸 2. Function Annotations (Type Hints in Functions)
# ------------------------------------------------------------
# Syntax: def function_name(param: type) -> return_type:

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

# Using the function
result = greet("Bob")        # This is valid
# wrong: int = greet("Bob")  # This would raise a warning in static type checker

# ------------------------------------------------------------
# 🔸 3. Class with Type Hints
# ------------------------------------------------------------
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

# Creating object
p1 = Person("Alice", 30)

# ------------------------------------------------------------
# 🔸 4. Type Hints for Collections
# ------------------------------------------------------------
from typing import List, Tuple, Dict, Set

names: List[str] = ["Alice", "Bob"]            # List of strings
coords: Tuple[float, float] = (3.5, -2.0)       # A tuple with two floats
ages: Set[int] = {23, 42, 31}                   # Set of integers
data: Dict[str, float] = {"a": 1.0, "b": 2.5}  # Dict with string keys and float values

# ------------------------------------------------------------
# 🔸 5. Modern Python (3.9+) - Built-in Generics
# ------------------------------------------------------------
values: list[int] = [1, 2, 3]                     # Same as List[int] but modern syntax
mapping: dict[str, int] = {"x": 1, "y": 2}     # Dictionary with str keys and int values

# ------------------------------------------------------------
# 🔸 6. Tuple Special Meaning
# ------------------------------------------------------------
fixed: tuple[int, str] = (5, "hello")            # Tuple of exactly 2 elements (int, str)
repeating: tuple[int, ...] = (1, 2, 3, 4)         # Tuple of any length, all int

# ------------------------------------------------------------
# 🔸 7. Union and Optional (Multi-Type Support)
# ------------------------------------------------------------
from typing import Union, Optional

def stringify(num: Union[int, float]) -> str:
    """Accepts int or float and returns a string."""
    return str(num)

# Newer Python (3.10+) allows using |
def stringify_v2(num: int | float) -> str:
    return str(num)

# Optional is just shorthand for Union with None
def find_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# ------------------------------------------------------------
# 🔸 8. ClassVar for Class-level Variables
# ------------------------------------------------------------
from typing import ClassVar

class Starship:
    stats: ClassVar[Dict[str, int]] = {}  # Shared by all instances
    fuel: int                             # Instance variable

# ------------------------------------------------------------
# 🔸 9. Legacy Style (Type Comments)
# ------------------------------------------------------------
# Old way of doing type hints in Python 2 or before PEP 526
logger = None  # type: str

# New way (modern style):
logger2: str = "Logger initialized"

# ------------------------------------------------------------
# 🧠 Note:
# All these type hints are ignored at runtime unless explicitly checked.
# But they are super helpful for code readability, editor support, and catching bugs early!

# End of Tutorial
