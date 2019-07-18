class Solution():
    def isPalindrome(self,Number):
                n=Number
                if Number >= 0:
                    Reverse = 0
                    while (Number > 0):
                        Reminder = Number % 10
                        Reverse = (Reverse * 10) + Reminder
                        Number = Number //10
                    
                    if(Reverse==n) :
                        return True
                    else:
                        return False
                else:
                    return False

num=121
s=Solution()
print(s.isPalindrome(num))
        
