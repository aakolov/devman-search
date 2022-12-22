from random import sample

def s(list_, target):
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            left = middle + 1
        elif list_[middle] > target:
            right = middle - 1
        else:
            return middle
    return

def input_and_check(min, max):
    i = False
    while not i:
        try:
          value = int(input(f'Pick an integer number between {min}-{max}: '))
          if value not in range(min, max + 1):
              print('You have entered number out of the range')
          else:
              i = True  
        except ValueError as ve:
          print('Please input integer number not string or float')
    return value
    
if __name__ == "__main__":
    min = 0
    max = 100
    step = 2
    list_len = 10
    rand_list = sorted(sample(range(min, max + 1, step), list_len))

    target = input_and_check(min, max)
    target_index = s(rand_list, target)
    print(f'List: {rand_list}')
    if target_index is not None:
        print(f'Found {target} in index {target_index}')
    else:
        print(f'Cannot find {target} in the list')