class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_=''
        for i in s:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
                str_+=i.lower()
        print(str_,str_[::-1])
        return str_ == str_[::-1]

        