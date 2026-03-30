class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''note: for w1 and w2 we need to make sure the first diff char 
        from both the words should follow the given alien order
        eg: w1="abc" w2="acda"
        here first we need to make sure both chars are not equal
        second we just need to check the first diff char from both the words
        from eg: a and a equal
        b and c not equal so we should compare this only if this order is correct break the loop
        else return false
        cause we care about the first diff char 
        '''

        order_index={char:i for i, char in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2=words[i], words[i+1]

            for j in range(len(w1)):
                if j==len(w2):
                    return False #cause if len of w2 is < len of w1 then w2 should come first 
                if w1[j]!=w2[j]:
                    if order_index[w1[j]]>order_index[w2[j]]:
                        return False
                    else:
                        break  #here the chars following the order no need to check all chars
        return True
        