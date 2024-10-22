def guessing_words(words):
    attempt=4
    while attempt>0:
        user=input("guess the word:").lower()
        if user in words:
            print('u guess the correct word')
            return True #u won the game
        else:
            attempt-=1
            if attempt>0:
                print(f'enter the correct word only {attempt} attempt has left')
    
    print('all attempt have been finished, beeter try next time')
    print('u have lost the game')
    return False # u loosw the game

words=['cricket','football','basketball','tennis','badmintion']
value= guessing_words(words)
print(value)
    