def uniq_add(my_list=[]):
    res = 0
    throwaway = [res += ele for ele in set(my_list)]
    return res
