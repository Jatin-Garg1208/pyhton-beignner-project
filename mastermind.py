import random

o_num = random.randrange(1000,10000)
guess_number = int(input("Enter the guess number: "))

guess_try=1
if(o_num==guess_number):
   print(f"Hurray! you guess the right answer in {guess_try} try")

while(guess_number != o_num):
   o_num=str(o_num)
   guess_number=str(guess_number)
   count=0
   counter=['x']*4

   for i in range(0,4):
      if(o_num[i]==guess_number[i]):
         count+=1
         counter[i]=o_num[i]
      else:
         continue
   if(count == 0):
    print(f"Sorry Better luck next time, there is no corrected digit")
   else:
      print(f"Sorry Better luck next time, {counter} are the corrected digit")
   guess_try+=1
   guess_number = int(input("Enter the guess number "))
   o_num=int(o_num)

if(o_num==guess_number):
   print(f"Hurray! you guess the right answer in {guess_try} try")

