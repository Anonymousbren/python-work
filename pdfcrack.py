import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("C:\Users\BAHAGO\Documents\opsm.pdf")]

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("sample.pdf", password=password) as pdf:
            print("\n[+] password found:", password)
            break
    except pikepdf._qpdf.passwordError as e:
        # wrong password, just coontinue with the loop
        continue