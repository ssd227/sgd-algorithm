排序的稳定性
A stable sort preserves the relative order of items with equal keys.

A. Insertion sort and mergesort (but not selection sort or shellsort).


具有排序一致性
- 插入排序、merge sort
- 不会打乱相同key的相对位置。 但要注意 merge时的 <= 操作，
保证left_sort和right_sort的一致性

另一个问题？

    java Uses tuned quicksort for primitive types; tuned mergesort for objects.
    Why use different algorithms for primitive and reference types?

    The most likely reason: quicksort is not stable, i.e. equal entries can change their relative position during the sort; among other things, this means that if you sort an already sorted array, it may not stay unchanged.
    Since primitive types have no identity (there is no way to distinguish two ints with the same value), this does not matter for them. But for reference types, it could cause problems for some applications. Therefore, a stable merge sort is used for those.
    OTOH, a reason not to use the (guaranteed n*log(n)) stable merge sort for primitive types might be that it requires making a clone of the array. For reference types, where the referred objects usually take up far more memory than the array of references, this generally does not matter. But for primitive types, cloning the array outright doubles the memory usage.
    
