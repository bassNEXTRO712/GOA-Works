#1) შექმენით სია, რომელსაც შეინახავთ ცვლადში სახელად friends.
#  მაგ სიაში უნდა შეინახოთ მინიმუმ 5 მეგობრის სახელი. პირველ
#  რიგში გამოიტანეთ თქვენი საუკეთესო მეგობრის სახელი ინდექსების დახმარებით.
#  დაბეჭდეთ სია. შეცვლაეთ მე-3 ინდექსზე მყოფი სახელი ახალით და დაბეჭდეთ სია. 
# საბოლოოდ დაბეჭდეთ მთლიანი სიის სიგრძე

friends = ["Nika", "Giorgi", "Luka", "Lasha", "Dima"]

friends[2] = "Mari"
print(friends)

#შექმენით მანქანების სია, სადაც გამოიყენებთ ერთ-ერთ ფუნქციას, რომ სიაში დაამატოთ ახალი მანქანა.

cars = ["Ferari", "Lamborghini", "Suzuki", "Audi", "Isuzu"]

cars.append("Dodge")
print(cars)

#ეხლით არ უნდა ჩაწეროთ!!!

#3) შექმენით რიცხვების სია სადაც გექნებათ მინიმუმ ხუთი რიცხვი. 
# შეცვლაეთ ამ სიის პირველი ელემენტი და გაუტოლეთ ის 50-ს.
#  შემდეგ კი გამოიტანეთ სიიდან პირველი და ბოლო რიცხვის ჯამი

numbers = [1,2,3,4,5] 
numbers[0] = 50
#print(numbers)
numbers = numbers[0] + numbers[4] 
print(numbers)