#შექმენი რაიმე რიცხვების ლისთი და შემდგომ for loop-ის საშუალებით დაპრინტე ამ რიცხვების ჯამი
nums = [1, 2, 3, 4, 5, 6, 7, 8]
total=0
for i in nums:
    total += i
print(total)




#შექმენი რაიმე რიცხვების ლისთი და შემდგომ while loop-ის საშუალებით დაპრინტე ამ რიცხვების ჯამი,
nums = [1, 2, 3, 4, 5, 6, 7, 8]
total = 0
index = 0
while index < len(nums):
    total += nums[index]
    index += 1
    print(index)


#გააკეთე ინფუთის ცვლადი სადაც მომხმარებელი შეიყვანს რაიმე სტრინგს, შემდგომ შენ უნდა დაპრინტო ეს სტრინგი ასოებად,
user_input = input("enter your word: ")
for i in user_input:
    print(i)



#გადმოგეცემა მასივი: nums = [1, 2, 3, 4, 5, 22, 66, 7, 21, 23] გადაუყევი ამ ლისთს ფორ ლუპით და გამოპრინტე მხოლოდ ლუწი რიცხვები
for i in nums:
    if i %2 ==0:
        print(i)




#While loop-ის გამოყენებით გააკეთე პაროლის შემოწმება, ცვლადში შეინახე პაროლი, შემდგომ კი მომხმარებელს შემოატანინე პაროლი, ვაილ ლუპი იმუშავებს იქამდე სანამ პაროლი არ იქნება სწორი, მაგრამ თუ 3 ჯერ შეიყვანა არასწორად, გაჩერდეს ვაილლუპი      
password = "123"
guess = 0
incorect = 0
while guess != password:
    guess = input("enter pin")
    if guess == password:
        print("you win")
    elif guess != password:
        incorect += 1
    elif icorect ==3:
        print("game over")
        break











