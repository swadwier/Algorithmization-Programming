# blocks = [1,2,3,4,6,4,7,8]
# blocks.sort()
# counter = 0
# counter2 = 0
# for k in range(len(blocks)-1):
#     counter = 0
#     for i in range(len(blocks)-1):
#         counter2 += 1
#         if blocks[i] > blocks[i+1]:
#             blocks[i], blocks[i+1] = blocks[i+1], blocks[i]
#             counter += 1
#         else:
#             continue
#     if counter == 0:
#         break
# print(blocks, counter, counter2)
import copy


def bubble_sort(blocks):
    sorted_blocks = copy.deepcopy(blocks)
    counter = 0
    counter2 = 0
    for k in range(len(sorted_blocks)-1):
        counter = 0
        for i in range(len(sorted_blocks)-1):
            counter2 += 1
            if sorted_blocks[i] > sorted_blocks[i+1]:
                sorted_blocks[i], sorted_blocks[i+1] = sorted_blocks[i+1], sorted_blocks[i]
                counter += 1
            else:
                continue
        if counter == 0:
            break
    return sorted_blocks, counter, counter2
