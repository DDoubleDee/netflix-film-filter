def search(sortedlist, usersearch, usersearchtitleon, usersearchcountryon, usersearchgenreon, usersearchactoron, usersearchdescon):
    searchlist = []
    if usersearchtitleon:
        for movie in sortedlist:
            if usersearch.lower() in movie[3].lower():
                searchlist.append(movie)
    if usersearchcountryon:
        for movie in sortedlist:
            if usersearch.lower() in movie[6].lower():
                searchlist.append(movie)
    if usersearchgenreon:
        for movie in sortedlist:
            if usersearch.lower() in movie[11].lower():
                searchlist.append(movie)
    if usersearchactoron:
        for movie in sortedlist:
            if usersearch.lower() in movie[5].lower():
                searchlist.append(movie)
    if usersearchdescon:
        for movie in sortedlist:
            if usersearch.lower() in movie[12].lower():
                searchlist.append(movie)
    return searchlist
