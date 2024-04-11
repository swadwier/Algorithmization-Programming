import linear_search_func
import binar_search_func
import bubble_search
import otbor_sort
import quick_sort

# blocks = [3, 4, 5, 7, 9, 1, 12, 15, 16]
blocks = [1, 2, 3, 4, 6, 4, 7, 8]
block_number = int(input())

index, counter = linear_search_func.get_block_by_index_linear(blocks, block_number)
if index is None:
    print(f"(linear) There isn't block #{block_number} in range, counter = {counter}")
else:
    print(f"(linear) Yes, block #{block_number} in range with index {index}, counter = {counter}")

index, counter = binar_search_func.get_block_by_index_binary(blocks, block_number)
if index is None:
    print(f"(binar) There isn't block #{block_number} in range; counter = {counter} \n")
else:
    print(f"(binar) Yes, block #{block_number} in range with index {index}; counter = {counter} \n")


sorted_blocks, swaps, iterations = bubble_search.bubble_sort(blocks)
print(f"(bubble) \nBlocks: {blocks}")
print(f"Sorted Blocks: {sorted_blocks}")
print(f"Number of swaps: {swaps}")
print(f"Number of iterations: {iterations} \n")

array_of_numbers = otbor_sort.sortirovka(blocks)
print(f"(otbor) {array_of_numbers} \n")

print(f"(quick) {quick_sort.quick_sort(blocks)}")
