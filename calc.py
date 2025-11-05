def add(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    return a + b

def subtract(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    return a - b

def multiply(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    return a * b


if __name__ == "__main__":
    x, y = 5, 3
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
