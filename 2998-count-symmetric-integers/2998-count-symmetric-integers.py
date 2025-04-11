class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        l=str(low)
        h=str(high)
        count=0
        for i in range(low,high+1):
            t=str(i)
            if len(t)%2==0:
                a=t[:len(t)//2]
                b=t[len(t)//2:]
                s1=0
                s2=0
                for i in a:
                    s1+=int(i)
                for i in b:
                    s2+=int(i)
                if s1==s2:
                    count+=1
        return count


                

        