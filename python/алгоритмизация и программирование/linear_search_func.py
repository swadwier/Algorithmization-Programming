# block_number = int(input())  # number_for_searching
def get_block_by_index_linear(block, block_number):
    counter = 0
    for i in block:
        counter += 1
        if i == block_number:
            return block.index(i), counter
    return None, counter
