#გააკეთე პატარა თამაში, შექმენი ცვლადი number და გადაეცი რაიმე integer მნიშვნელობა (რაიმე რიცხვი) შემდეგ შექმენი guess ცვლადი სადაც მომხმარებელი input()-ის საშუალებით შემოიტანს მნიშვნელობას, While loop უნდა მუშაობდეს იქამდე სანამ მომხმარებელი არ გამოიცნობს ჩაფირებულ რიცხვს (number ცვლადში შენახულ რიცხვს)
number = 50
guess = 0
while guess != number:
    guess = int(input("შემოიტანეთ რიცხვი"))
    if guess < number:
        print("it's to small")
    if guess > number:
        print("it's to big") 
    if guess == number:
        print("you win")
print(3<1)
        

