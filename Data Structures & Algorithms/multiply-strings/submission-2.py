class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1[0],num2[0]):
            return "0"
        num1_len=len(num1)
        num2_len=len(num2)
        res=[0]* (num1_len+num2_len)
        num1,num2=num1[::-1],num2[::-1]
        for i in range(num1_len):
            for j in range(num2_len):
                digit=int(num1[i])*int(num2[j])
                res[i+j]+=digit
                res[i+j+1]+=res[i+j]//10
                res[i+j]=res[i+j]%10
        res,begin=res[::-1],0
        while begin<len(res) and res[begin]==0:
            begin+=1
        res=map(str,res[begin:])
        return "".join(res)

