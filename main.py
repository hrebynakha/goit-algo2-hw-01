"""
Пошук максимального та мінімального елементів

Реалізуйте функцію, яка знаходить максимальний та мінімальний елементи в масиві,
використовуючи метод «розділяй і володарюй».

Функція приймає масив чисел довільної довжини.
Використано рекурсивний підхід.
Повертається кортеж значень (мінімум, максимум).
Складність алгоритму — O(n).


=============================


Пошук k-го найменшого елемента



Реалізуйте алгоритм пошуку k-го найменшого елемента в несортованому масиві,
 використовуючи принцип Quick Select.



Умови виконання

Функція має приймати масив чисел та число k.
Необхідно використати підхід з вибором опорного елемента pivot .
Масив не має бути повністю відсортований.
Очікувана складність в середньому випадку має складати O(n).

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


class QuickSelectView:
    """Class to view step by step how work quick select algorithm"""

    def __init__(self, arr: list, k: int, step_mode: bool = True) -> None:
        if not 1 <= k <= len(arr):
            raise ValueError(
                "k-th element can't be greater than array length or less than 1"
            )
        self.arr = arr
        self.k = k  # 1 based element
        self.left = 0
        self.right = len(self.arr) - 1
        self.step_mode = step_mode

    def partition(self, left: int, right: int) -> int:
        """Partition function for QuickSelect algorithm."""
        pivot = self.arr[right]
        self.show("=======================>>", end=None)
        self.show(f"Pivot is {right+1} element", color="95", end=None)
        i = left - 1
        for j in range(left, right):
            self.view(i, j, pivot_idx=right)
            self.step(f"{self.arr[j]} <= {pivot} ?")
            if self.arr[j] <= pivot:
                i += 1
                if i != j:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    self.view(i, j, right, "<", ">")
                    self.step(f"Swapped {i+1} and {j+1} elements!", color="93")

        if self.arr[i + 1] != self.arr[right]:
            self.view(i + 1, right, right, "<", ">")
            self.step(f"Swap {i+2} element with {right+1} element")
            self.arr[i + 1], self.arr[right] = self.arr[right], self.arr[i + 1]
        return i + 1

    def select(self) -> int:
        """Select the first min k-el in unsorted array"""
        while self.left < self.right:
            pivot_idx = self.partition(left=self.left, right=self.right)
            self.view(pivot_idx, -1, start="?", end="?")
            self.step(f"We looking for {pivot_idx +1} element??")

            if (pivot_idx + 1) == self.k:
                self.view(pivot_idx, -1)
                self.step(f"We found ... {self.k} element!!", color="92")
                return self.arr[pivot_idx]

            self.show(" ..No!  ", color="91")

            if pivot_idx > (self.k - 1):
                self.right = pivot_idx - 1
            else:
                self.left = pivot_idx + 1

        self.show("Looking element in looking postiton!", color="93", end=None)
        return self.arr[self.k - 1]

    def show(self, text, color="1", end="") -> None:
        """Print text without new line"""
        print(f"\033[{color}m{text}\033[0m", end=end)

    def step(self, text, color="94") -> None:
        """Wait for input"""
        if self.step_mode:
            input(f" ||| \033[{color}m{text}\033[0m")
        else:
            print(f" ||| \033[{color}m{text}\033[0m")

    def view(
        self, current_i, current_j=None, pivot_idx=None, start="[", end="]"
    ) -> None:
        """Show curent array info"""
        for i, _ in enumerate(self.arr):
            if pivot_idx == i:
                print(f"\033[95m{start}{self.arr[i]}{end}\033[0m", end="")
            elif current_i == i:
                print(f"\033[91m{start}{self.arr[i]}{end}\033[0m", end="")
            elif current_j == i:
                print(f"\033[4m{start}{self.arr[i]}{end}\033[0m", end="")
            else:
                print(f"\033[93m[{self.arr[i]}]\033[0m", end="")


def main() -> None:
    """main app enrtypoint"""
    print(find_min_max([9, 7, 220, -89, 0]))  # -89, 220
    print(find_min_max([38, 27, 90, 4]))  # 4, 90
    print(find_min_max([1]))  # 1, 1
    sorted_arr = [11, 12, 13, 14, 15, 16, 17]
    unsorted_arr = [2, 0, 1, 8, 9, 4, 3, 5, 7, 6]
    qsv = QuickSelectView(sorted_arr, 2)
    print(qsv.select())
    qsv2 = QuickSelectView(unsorted_arr, 3)
    print(qsv2.select())


if __name__ == "__main__":
    main()
