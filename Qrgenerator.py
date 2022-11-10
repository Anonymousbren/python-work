import random
import qrcode


def generate_password(n_characters):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '1234567890'
    Symbols = '!@#$%&*?()[]{}='
    all_characters = lower + upper + number +Symbols
    
    
    password = ''.join(random.sample(all_characters, n_characters))
    return password

def image_qr(password):
    filename = input('Digit name password: ')
    img = qrcode.make(password)
    img.save(filename + '.png')
    
    
def run():
    characters = int(input('digit number of characters: '))
    password = generate_password(characters)
    print(f'your new password is: {password}')
    image_qr(password)
    print('the password was save as Qr code image')
    
    
    if __name__ == '__main__':
        run()