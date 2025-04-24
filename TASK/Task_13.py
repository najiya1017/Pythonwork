def is_anagram(string,substring):
    is_anagram=True
    length=0
    for ch in substring:
        if substring.count(ch)==string.count(ch):
            length+=substring.count(ch)
        else:
            is_anagram=False
            break

    if len(string)==length:
        is_anagram=True

    return is_anagram


string=input("S:")
substring=input("t:")
print(is_anagram(string,substring))