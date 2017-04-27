ori_lst = list(range(1,11))

def movebackward():
    ori_lst.append(ori_lst.pop(0))
    return ori_lst

def application_times(x):
    for i in x:
        movebackward()


print (application_times(3))
