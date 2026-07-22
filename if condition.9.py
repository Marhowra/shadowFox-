australia=["sydney","melbourne","brisbane","perth"]
UAE=["duabi","abu dhabi","sharjah","ajman"]
india=["mumbai","banglore","chennai","delhi"]
city=input("Enter a city name:")
if city in australia :
    print(city,"is in australia")
elif city in UAE:
    print(city,"is in UAE")
elif city in india:
    print(city,"is in india")
else:
    print("city not found")
