def separateNumbers(s):
    c=0
    r=len(s)//2
    if s[0]==0 or len(s)==1:
        print("NO")
    elif len(s)==2:
        if int(s[1])-int(s[0])==1:
            print("YES",s[0])
        else:
            print("NO")
    else:
        for i in range(r+1):
            q = (s[0:i+1:1])
            t = int((s[0:i+1:1]))
            l=len(q)
            while (l<=len(s)):
                if s[l:l+len(str(t+1)):1]==str(t+1):
                    t=t+1
                    l=l+len(str(t))
                else:
                    break

            if l==len(s):
                c=-1
                break
        
        if c==-1:
            print("YES",q)
        else:
            print("NO")
            


    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
