"""
Пошук максимального та мінімального елементів

Реалізуйте функцію, яка знаходить максимальний та мінімальний елементи в масиві,
використовуючи метод «розділяй і володарюй».

Функція приймає масив чисел довільної довжини.
Використано рекурсивний підхід.
Повертається кортеж значень (мінімум, максимум).
Складність алгоритму — O(n).

"""


def find_min_max(
    arr: list[int],
) -> tuple[int, int]:
    """Function to find in array min and max element, return min and max as tuple"""
    if not arr:
        raise ValueError("Array can't be empty")

    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left, right = arr[0:mid], arr[mid:]

    min_l, max_l = find_min_max(left)
    min_r, max_r = find_min_max(right)

    min_ = min_l if min_l < min_r else min_r
    max_ = max_l if max_l > max_r else max_r
    # can replace this  with min and max
    # return min(min_l, min_r), max(max_l, max_r)
    return min_, max_


def main() -> None:
    """main app enrtypoint"""
    print(find_min_max([9, 7, 220, -89, 0]))  # -89, 220
    print(find_min_max([38, 27, 90, 4]))  # 4, 90
    print(find_min_max([1]))  # 1, 1
    print(find_min_max([]))  # ValueError: Array can't be empty


if __name__ == "__main__":
    main()
