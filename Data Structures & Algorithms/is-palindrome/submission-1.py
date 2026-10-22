class Solution:
    def isPalindrome(self, s: str) -> bool:
        lookup = 'abcdefghijklmnopqrstuvwxyz0987654321'
        lower = s.lower()
        k = ''
        for i in range(0,len(lower)):
            if(lower[i] in lookup):
                k += lower[i]

        for j in range(0,len(k)):
            forward = j 
            backward = len(k)-(j+1)
            print(k[forward], k[backward])
            if(k[forward]!=k[backward]):
                return False
        return True
        