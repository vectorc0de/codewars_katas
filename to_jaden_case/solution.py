def to_jaden_case(strings):
    ret_str = []
    for word in strings.split():
        ret_str.append(word[0].upper() + word[1:].lower())

    ret_str = " ".join(ret_str)
    return ret_str

# str = "How can mirrors be real if our eyes aren't real"
# to_jaden_case(str)