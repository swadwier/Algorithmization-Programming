import copy


def quick_sort(blocks):
    sorted_blocks = copy.deepcopy(blocks)

    if (len(blocks) == 1) or (len(blocks) == 0):
        return sorted_blocks

    oporny_block = sorted_blocks[0]

    smaller = list(filter(lambda x: x < oporny_block, sorted_blocks))
    bigger = list(filter(lambda x: x > oporny_block, sorted_blocks))
    current = [i for i in sorted_blocks if i == oporny_block]

    return quick_sort(smaller) + current + quick_sort(bigger)




