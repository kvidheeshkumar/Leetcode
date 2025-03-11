class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d={"a":-1,"b":-1,"c":-1}
        ans=0
        for index,character in enumerate(s):
            d[character]=index
            ans+=min(d["a"],d["b"],d["c"])+1
        return ans
        