with open('a.avi','rb') as read_f,open('b.avi','wb') as write_f:
    for line in read_f:
        write_f.write(line)