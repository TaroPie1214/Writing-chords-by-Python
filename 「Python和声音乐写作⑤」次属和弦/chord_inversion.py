def chord_inversion(root):
    if root == 'F' or root == 'G' or root == 'A' or root == 'B':
        format = [1,2,3]
        root_base = -1
    else:
        format = [0,1,2]
        root_base = 0
    return format, root_base