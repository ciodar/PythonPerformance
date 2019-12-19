def insertion_sort(v):
    for j in range(1, len(v)):
        key = v[j]
        i = j - 1
        while (i >= 0) and (v[i] > key):
            v[i+1] = v[i]
            i = i - 1
        v[i+1] = key


