import hashlib
import os

def hash_password(password, salt):
    hash_unsalted = hashlib.sha256(password.encode('UTF-8')).hexdigest()
    print(f"Unsalted: {password} \n{hash_unsalted}")

    salted_password = password + salt
    hash_salted = hashlib.sha256(salted_password.encode('UTF-8')).hexdigest()
    print(f"Salted: {salted_password} \n{hash_salted}")

def hash_file(file):
    with open(file) as f:
        data = f.read()
        hash_data = hashlib.sha256(data.encode('UTF-8')).hexdigest()
        print(hash_data)

# Sample
#
# password = "atlas"
# salt = "jam"
# hash_password(password, salt)
#
# hash_file()
#
# file = "detailed.csv"
# hash_file(file)


dir_path = 'C:\\Users\Panini\Documents\PythonEssentials\TestFolder\\'
file_list = []

for root, dirs, files in os.walk(".", topdown=True):
   for name in files:
      file_list.append(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
for files in file_list:
    try:
        hash_file(files)
        #print(f'{hash_file(files)}')
    except:
        continue