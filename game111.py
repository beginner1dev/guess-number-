import random

guess_me = int(input('ye adad entekhab konid (1 , 99):  '))
guess_pc = random.randint(1,99)
print('guess_pc= ' , guess_pc)
low = 1
high = 99
print('low= ' , low)
print('high= ' , high)

while guess_me != guess_pc :
    
    if guess_pc > guess_me : 
        print('mine little')
        high = guess_pc - 1
        print('low= ' , low)
        print('high= ' , high)
    
    elif guess_pc < guess_me :
        print('mine biger')
        low = guess_pc + 1
        print('low= ' , low)
        print('high= ' , high)

    guess_pc = random.randint(low , high)
    print('guess_pc= ' , guess_pc)

print('wowwwwww!!!!! you were right!!!')