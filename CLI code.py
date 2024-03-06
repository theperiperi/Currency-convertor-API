#menu
import requests 

while True:
    print("1.conversion,2.adding")
    target_currency=input("convert this to what currency?")
    user_amount=float(input("enter amount"))
    url="http://localhost:8000/exchange"
    response=requests.get(url,params={"source_currency":"INR",
                                      "target_currency":target_currency,
                                      "user_amount":user_amount})
    data=response.json()
    print(user_amount,target_currency,"in INR id",data["amount"])
