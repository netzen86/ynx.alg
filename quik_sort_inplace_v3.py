# id посылки 69575638
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Competitor:
    """Класс описывающий участника соревнований"""
    name: str
    task: int
    penalty: int

    def __str__(self) -> str:
        return self.name


def partition(
    array: List[Competitor],
    start: int,
    end: int,
    compare_func: Callable[..., bool]
) -> int:
    """Функция разделения массива на части"""
    # точка отталкивания
    pivot: Competitor = array[start]
    # левый указатель
    low: int = start + 1
    # правый указатель
    high: int = end
    while True:
        # если элемент больше pivot перемещаем правый указатель влево
        # логика сравнения описана в lamda функции
        while low <= high and compare_func(array[high], pivot):
            high = high - 1
        # если элемент меньше pivot перемещаем левый указатель вправо
        while low <= high and not compare_func(array[low], pivot):
            low = low + 1
        # нашли элементы в неправильном положении свапнули их
        if low <= high:
            array[low], array[high] = array[high], array[low]
        # левый казатель больше правого значит элементы отсортированы
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(
    array: List[Competitor],
    start: int,
    end: int,
    compare_func: Callable[..., bool]
) -> None:
    """Функция быстрой сортировки"""
    # базовый случай, выход из рекурсии когда указатели встретились
    if start >= end:
        return
    # разделяем массив на части
    part: int = partition(array, start, end, compare_func)
    # рекурсивно вызываем quick_sort()
    quick_sort(array, start, part - 1, compare_func)
    quick_sort(array, part + 1, end, compare_func)


if __name__ == '__main__':
    array: List[Competitor] = []
    number_competitor: int = int(input())

    for competitor in range(number_competitor):
        array.append(
            Competitor(
                *[
                    int(item)
                    if item.isdigit()
                    else item
                    for item in input().split()
                ]
                )
            )

    quick_sort(
        array,
        0,
        len(array) - 1,
        # функция сравнения выдает True если соблюдены условия сравнения
        lambda x, y: x.task < y.task
        if x.task != y.task
        else (
            x.penalty > y.penalty
            if x.penalty != y.penalty
            else (x.name > y.name)
        ),
    )
    for person in array:
        print(person)
