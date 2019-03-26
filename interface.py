def print_blue(text):
  text = '\033[1;34m' + text + '\033[1;m'
  print(text)

def print_green(text):
  text = '\033[1;32m' + text + '\033[1;m'
  print(text)

def print_magenta(text):
  text = '\033[1;35m' + text + '\033[1;m'
  print(text)

print("\n")
print_green("- Choose algorithm -")
print_magenta("[1] ElGamal \t [2] ECC")
in_algo = input("Enter Choice: ")

print("\n================")
print_green("- Choose operation -")
print_magenta("[1] Encrypt \t [2] Decrypt")
in_op = input("Enter Choice: ")

print("\n================")
print_green("- Enter public key location -")
in_key_pub = input("Enter file location: ")

print("\n================")
print_green("- Enter private key location -")
in_key_pri = input("Enter file location: ")

print("\n================")
print_green("- Enter target file -")
in_file = input("Enter file: ")

if in_algo == 1:
  pass
elif in_algo == 2:
  pass