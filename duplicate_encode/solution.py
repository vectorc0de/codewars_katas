def duplicate_encode(word):
    ret_str = []
    i = 0
    word = word.lower()
    for char in range(len(word)):
        if word.count(word[i]) == 1:
            ret_str.append("(")
        else:
            ret_str.append(")")
        i += 1

    return "".join(ret_str)

# )())())
# duplicate_encode("Success")