import heapq


def top_n_largest(items, n):
    heap = []

    for i in range(n):
        heap.append(items[i])
    heapq.heapify(heap)
    for i in range(n, len(items)):
        if items[i] > heap[0]:
            heapq.heapreplace(heap, items[i])

    return heap
