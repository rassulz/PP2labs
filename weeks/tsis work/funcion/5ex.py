def permute(data, i, length):
    if i == length:
        print("".join(data))
    else:
        for j in range(i, length):
            # Swap the ith and jth character
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            # Swap back the ith and jth character to restore the original string
            data[i], data[j] = data[j], data[i]

def all_permutations(string):
    permute(list(string), 0, len(string))

input_string = "abc"
all_permutations(input_string)
