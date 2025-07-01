#შექმენი რაიმე ლისთი
fruit = ["banana","orange","lemon","cherry","peach","apple"]

#ამ ლისთში ჩაამატე ელემენტები(.append())
fruit.append("blueberry")
print(fruit)


# ამოშალე ლისთიდან ელემენტები (.remove())
fruit = ["banana","orange","lemon","cherry","peach","apple"]
fruit.remove("orange")
print(fruit)


#ამოშალე ლისთიდან ელემენტები მეორე გზით(.pop() არ დაგავიწყდეს ამ შემთხვევაში ელემენტს ინდექსის საშუალებით ვშლით)
fruit = ["banana","orange","lemon","cherry","peach","apple"]
fruit.pop(2)
print(fruit)


#შეცვალე ლისთის რომელიმე ელემნტი, ჩააცვლე ახალი ელემენტით
fruit = ["banana","orange","lemon","cherry","peach",]
fruit[4]= "mango"
print(fruit)


#გამოპრინტე ამ ლისთის ელემენტები ინდექსების საშუალებით
fruit = ["banana","orange","lemon","cherry","peach","apple"]
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
print(fruit[5])





