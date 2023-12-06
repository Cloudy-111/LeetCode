from queue import Queue


def predictPartyVictory(senate):
    q1 = Queue()
    q2 = Queue()
    for i in range(len(senate)):
        if senate[i] == 'D':
            q1.put(i)
        else:
            q2.put(i)
    tmp = len(senate) - 1

    while not q1.empty() and not q2.empty():
        print(list(q1.queue))
        print(list(q2.queue))
        tmp += 1
        s1 = q1.get()
        s2 = q2.get()
        if s1 < s2:
            q1.put(tmp)
        else:
            q2.put(tmp)
    if q1.empty():
        return 'Radiant'
    else:
        return 'Dire'


senate = 'RRRRRRRRRD'
print(predictPartyVictory(senate))
