subsequence=input("s:")

Sequence=input("t:")

count=0

for ch in subsequence:

    if ch in Sequence and subsequence.count(ch)<=Sequence.count(ch):

        count+=1

print(True if count==len(subsequence) else False)


