import requests

token = input("Your token: ")
print("\n\nHouse: \n1 = Bravery \n2 = Brilliance \n3 = Balance\n\n")
house = input("House choice: ")

if house == "1":
    housefinal = 1

if house == "2":
    housefinal = 2

if house == "3":
    housefinal = 3

sess = requests.session()

headers = {
    'Authorization': str(token)
}

payload = {
    'house_id': str(housefinal)
}

rep = sess.post("https://discord.com/api/v8/hypesquad/online", json=payload, headers=headers)
if rep.status_code == 204:
    print("Success")
else:
    print("Failed")