class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        h=(n+1)//2
        minh=10**(h-1)
        maxh=10**(h)
        ans=0
        seen=set()
        for i in range(minh,maxh):
            palindrome=str(i)+str(i)[::-1][n%2:]
            sorted_digits=''.join(sorted(palindrome))
            if int(palindrome)%k!=0 or sorted_digits in seen:
                continue
            seen.add(sorted_digits)
            digitCount=collections.Counter(palindrome)
            #Leading zeroes are not allowed, so first digit is special
            fdc=n-digitCount['0']
            p=fdc*math.factorial(n-1)

            #For each repeated digit, divide the factorial of the frequency since permutations that swap identical digits don't create a new number

            for i in digitCount.values():
                p//=math.factorial(i)
            ans+=p
        return ans