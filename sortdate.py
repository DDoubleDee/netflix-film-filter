def sortdate(mlist, userdate):
    sortedlist = mlist
    if userdate == 1:
        sortedlist = sorted(mlist, reverse=True, key=lambda tup: tup[8])
    elif userdate == 2:
        sortedlist = sorted(mlist, key=lambda tup: tup[8])
    elif userdate == 3:
        sortedlist = sorted(mlist, key=lambda tup: tup[3])
    elif userdate == 4:
        sortedlist = sorted(mlist, reverse=True, key=lambda tup: tup[3])
    return sortedlist
