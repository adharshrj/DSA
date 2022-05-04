def palindrome(str):
    if str[::-1] == str:
        return True

def ispalindrome(str):
    first = 0
    last = len(str)-1
    if not str:
        return False
    elif len(str) == 1:
        return True
    else:
        while first<last:
            if str[first]!=str[last]:
                return False
            first+=1
            last-=1
        return True

print(ispalindrome("RACECAR"))
print(palindrome("RACECAR"))

    