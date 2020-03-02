from collections import Counter

phones = ["Iphone", "Samsung", "LG", "Iphone", "LG"]

count = Counter(phones)
print(count["Hello"])

text = "Раз два три четыре".lower().replace(" ", "")
count = Counter(text)
print(count)