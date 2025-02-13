def concatenation (list_word,w1):
    
    return [tuple(list(word)+[w1] )for word in list_word]


def shuffle (w1,w2):
    
    if len(w1)==0:
        return [w2]
    
    if len(w2)==0:
        return [w1]
    
    return concatenation(shuffle(w1[:-1],w2),w1[-1])+ concatenation(shuffle(w1,w2[:-1]),w2[-1])