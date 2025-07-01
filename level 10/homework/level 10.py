#შექმენი რაიმე ლისთი, სადაც გაქვს 5ელემენტი ამ ლისთში დაამატე 4 ელემეტი და ამოშალე ორი, შემდგომ გადაყუევი for loop-ით და გამოპრინტე ყველა ელემენტი
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers.append(70)
numbers.append(80)
numbers.append(90)

numbers.pop(2)

for num in numbers:
    print(num)