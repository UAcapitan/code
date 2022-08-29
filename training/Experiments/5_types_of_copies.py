
list_original: list[int] = [1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    # Shallow copy
    list_shallow_copy: list[int] = list_original

    # Deep copy
    list_deep_copy: list[int] = list_original.copy()

    list_original[0] = 10
    list_shallow_copy[-1] = 11
    
    print(list_original)
    print(list_shallow_copy)
    print(list_deep_copy)
