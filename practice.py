s = 10
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == s:
        print('you won my nigga')
        break
else:
    print('sorry bro you are wrong')    


