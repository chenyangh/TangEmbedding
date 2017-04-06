file_list = ['emotion.neg.0.txt', 'emotion.pos.0.txt']

with open('vocb.txt', 'w') as wf:
    voc_dict = {}
    for file in file_list:
        with open('data/'+file, 'r', encoding="ISO-8859-1") as rf:
            for word in rf.read().split():
                if word not in voc_dict:
                    voc_dict[word] = 1
                else:
                    voc_dict[word] += 1
    for voc in voc_dict:
        wf.write(voc + ' ' + str(voc_dict[voc]) + '\n')

