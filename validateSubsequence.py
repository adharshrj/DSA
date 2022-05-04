'''Given two non-empty arrays of integers, write a function that determines whether 
the second array is a subsequence of the first one. A subsequence of an array is a set 
of numbers that aren't necessarily adjacent in the array but that are in the same order 
as they appear in the array. For instance, the number [1, 3, 4] from a subsequence of the 
array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array 
itself are both valid subsequence of the array.'''

# Time O(N), Space O(1)
def validsubsequencefor(arr, seq):
    idx=0
    for value in arr:
        if value == seq[idx]:
            idx+=1
        if idx == len(seq):
            return True
    return False 

'''or return idx==len(seq)'''

def validsubsequencewhile(arr, seq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(arr) and seqIdx < len(seq):
        if arr[arrIdx] == seq[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(seq)