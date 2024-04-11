# blocks = [1,2,3,4,6,4,7,8]
# block_number = int(input())
# def get_block_by_index_binary(block, block_number):
#     block_first = block.copy()
#     block.sort()
#     counter = 0
#     while len(block):
#         middle = block[(len(block) // 2)]
#         if block_number < middle:
#             block = block[slice(0, block.index(middle))]
#             counter += 1
#             continue
#         if block_number > middle:
#             block.append(block[-1])
#             block = block[slice(block.index(middle)+1, -1)]
#             counter += 1
#             continue
#
#         if block_number == middle:
#             counter += 1
#             return block_first.index(block_number), counter
#
#         if block.index(middle)+1 > block_number:
#             counter += 1
#             return None, counter
#
#         elif block.index(middle)+1 == block_number:
#             counter += 1
#             return block_first.index(block_number), counter
#
#         return None, counter
import copy


def get_block_by_index_binary(block, block_number):
    block_first = copy.deepcopy(block)
    block_sort = copy.deepcopy(block)
    block_sort.sort()
    counter = 0
    while len(block_sort) > 0:
        middle_index = len(block_sort) // 2
        middle = block_sort[middle_index]
        if block_number == middle:
            counter += 1
            return block_first.index(middle), counter
        elif block_number < middle:
            block_sort = block_sort[:middle_index]
        else:
            block_sort = block_sort[middle_index + 1:]
        counter += 1
    return None, counter
# index, counter = get_block_by_index_binary(blocks, block_number)
# if index is None:
#     print(f"There isn't block #{block_number} in range; counter = {counter}")
# else:
#     print(f"Yes, block #{block_number} in range with index {index}; counter = {counter}")
