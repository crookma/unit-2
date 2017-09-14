# By: Mangus Crooke, last modified on 9-14-17, File name: unit 2 project.py, this program is a ChatBot
# ChatBot introduces itself

print('Hey, my name is Chatbot, whats yours?')
person = input('enter your name:')
print('Hey', person, 'its so nice to meet you')

# Asking where the user is from
location = input(person + "," + " " + 'Where are you from?')
print('Ive always wanted to go to', location)
favorite_number = 12
number = input("Hey" + " " + person + " " + "my favorite number is 12" + " " + 'whats is your whole favorite number?')

relate_numbers = int(favorite_number) * int(number) * 7
print('When our favorite numbers are multiplied by each other and then multiplied by 7 is', relate_numbers)

favorite_car = input(person + "," + " " + 'Whats your favorite car?')
car_cost = input('Nice Ive always wanted a' + " " + favorite_car + "," + " " + "also, how much does it cost?")
interst_rate = input('What is the yearly interest rate on that car?')
years = input('If you took a loan out on' + " " + favorite_car + "," + " " +
              "how long would it take you to pay off the loan?")
months = 12 * float(years)
interest = float(interst_rate)/100/12
payment = float(car_cost) * float(interest) / (1 - (1 + interest) ** -months)
total_sum = float(car_cost) + payment
print("If you bought the", favorite_car, "it would cost you", payment, "per month!", "which is a total of,", total_sum)
print("Anyhow, it was lovely talking to you", person + "!")
