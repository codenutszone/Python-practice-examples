class Solution():
    def reverse(self,Number):

                flag=False
                if Number < 0:
                     flag = True
                     Number=-1*Number

                Reverse = 0
                while (Number > 0):
                    Reminder = Number % 10
                    Reverse = (Reverse * 10) + Reminder
                    Number = Number //10

                num= -Reverse if (flag == True) else Reverse
                return num if num in range(-2**31,2**31-1) else 0
num=int(input("enter the integer number: "))
s=Solution()
print(s.reverse(num))
