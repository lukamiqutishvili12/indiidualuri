#1)შექმენი ლისთი შემდეგ კი for loop-ის საშუალებით გამოპრინტე თითოეული ელემენტი
fruit = ["banana","orange","lemon","cherry","peach","apple"]
for i in fruit:
    print(i)

#2)გაიმეორე პირველი დავალება თუმცა ამჯერად მეორე გზით, სადაც ვიყენებთ range-ს (range(len(names)):)
for i in range (len(fruit)):
    print(fruit[i])

#3)გააკეთე  რენდომ ხილების ლისთი, შემდეგ კი ჩაამატე ის ხილი რომელიც გიყვარს
fruit = ["banana","orange","lemon","cherry","peach","apple"]
fruit.append("grape")
print(fruit)

#4)ამავე ლისთიდან ამოშალე ის ხილი რომელიც ყველაზე ნაკლებად გიყვარს
fruit = ["banana","orange","lemon","cherry","peach","apple"]
fruit.remove("orange")
print(fruit)


#დაპრინტე ამ ლისთის სიგრძე (Lenght) მინიშნება: len()
my_list = [1,2,3,4,5]
print(len(my_list))



