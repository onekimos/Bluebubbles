print ("Akwaaba to my puzzle!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()


print("Okay! Lets play")
score = 0

answer = input("What does SV stand for? ").lower()
if answer == "single vision":
    print("Correct! ")
    score += 1

else:
    print('Incorrect!')


answer = input("What does PH stand for? ").lower()
if answer == "photo":
    print("Correct! ")
    score += 1

else:
    print('Incorrect!')


answer = input("What does FT28 stand for? ").lower()
if answer == "bifocals":
    print("Correct! ")
    score += 1

else:
    print('Incorrect!')


answer = input("What does HC stand for? ").lower()
if answer == "hard coat":
    print("Correct! ")
    score += 1

else:
    print('Incorrect!')

print('You got ' + str(score) +  ' questions correct!')
print('You got ' + str((score / 4) * 100) +  '%.')
