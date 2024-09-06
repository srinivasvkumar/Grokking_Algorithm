def cntlist(lt):
    if lt == []:
        return 0
    return 1 + cntlist(lt[1:])


print(cntlist([1,2,3,4]))



