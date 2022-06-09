def anagramsnlogn(s1, s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)

def anagramsn(s1, s2):
    if len(s1)!=len(s2):
        return False
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1
    
    for ch in s2:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch]=1

    for item in freq1:
        if item not in freq2 or freq1[item]!=freq2[item]:
            return False
    return True