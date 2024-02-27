def fnrc(s):
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return s[i]
    return "nil"

def fnrc_ans(s):
    d = {} # (1)
    n = len(s)
    for i in range(n): # (2)
        if s[i] in d:
            d[s[i]] += 1 # (3)
        else:
            d[s[i]] = 1 # (4)
    for i in range(n): # (5)
        if d[s[i]] == 1: # (6)
            return s[i] # (7)
    return None # (8)

print(fnrc_ans("abcxabcabc"))
print(fnrc("abcxabcabc"))
print(fnrc_ans("abacx"))
print(fnrc("abacx"))
print(fnrc_ans("xxaabb"))
print(fnrc("xxaabb"))
print(fnrc_ans("abybaxa"))
print(fnrc("abybaxa"))