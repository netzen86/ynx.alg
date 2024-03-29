def is_first_num_less(num_1, num_2):
    return num_1 < num_2

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i
    # заменим сравнение item_to_insert < array[j-1] на компаратор less
    while j > 0 and less(item_to_insert, array[j-1]):
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert

cards = [3, 7, 9, 2, 3]
insertion_sort_by_comparator(cards, is_first_card_weaker) 