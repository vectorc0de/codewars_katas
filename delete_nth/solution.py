def delete_nth(order,max_e):
    ret_list = []
    for element in order:
        if ret_list.count(element) < max_e:
            ret_list.append(element)

    return ret_list