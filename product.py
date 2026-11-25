import requests

url = "https://dummyjson.com/products"

response = requests.get(url)

data = response.json()

for product in data["products"]:
    
    print("ID:", product["id"])
    print("Title:", product["title"])
    print("Price:", product["price"])
    print("Category:", product["category"])
    print("Stock:", product["stock"])
    print("Images:", product["images"])
    print("---------------------------------------------")