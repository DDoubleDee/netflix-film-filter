def sortdate(mlist, userdate):
    if userdate == 1:
        sortedlist = sorted(mlist, reverse=True, key=lambda tup: tup[8])
    elif userdate == 2:
        sortedlist = sorted(mlist, key=lambda tup: tup[8])
    sortedlist = mlist
    return sortedlist
