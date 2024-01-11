from typing import Callable

def validate_and_add(numbers: list[int], number: int, predicate_fn: Callable[[int], bool]) -> list[int]:
    # if number % 2 == 0:
    # if predicate_fn(number):
    #     numbers.append(number)
    # return numbers
    return numbers + ([number] if predicate_fn(number) else [])

def validate_and_add_2[T](elements: list[T], element: T, predicate_fn: Callable[[T], bool]) -> list[T]:
    return elements + ([element] if predicate_fn(element) else [])

def is_even(n: int) -> bool:
    return n % 2 == 0

def main() -> None:
    numbers = [1, 2, 3]
    # names = ['ala', 'ola']
    print(validate_and_add(numbers, 21, lambda n: n % 2 == 1))
    print(numbers)
    # validate_and_add_2(names, 'a', is_even)

if __name__ == '__main__':
    main()