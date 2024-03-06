import pydantic
from fastapi import FastAPI
app=FastAPI()

exchange_rates={
    "USD":1.0,
    "INR":82.90,
    "EUR":0.84
}

#decorator
@app.get("/")

def root():
    return "Hello World"

@app.get("/exchange")

def exchange(source_currency:str,target_currency:str,user_amount:float):

    if source_currency not in exchange_rates or target_currency not in exchange_rates:
        return{
            "error":"I am a teapot"
        }
    
    source_rate=exchange_rates[source_currency]
    usd_amount=user_amount/source_rate
    dest_amount=usd_amount*exchange_rates[target_currency] 
    return {
        "amount":dest_amount
    }

#extanding pdantic basemodel
class ExchangeRate(pydantic.BaseModel):
    currency_id:str 
    rate:float 

@app.post("/add_exchange_rate")
def add_exchange_rate(exchange_rate:ExchangeRate):
    currency_id=exchange_rate.currency_id 
    value=exchange_rate.rate
    if currency_id in exchange_rates:
        return{
            "error":"currency already exists"
        }

    exchange_rate=[currency_id]=value 
    return {
        "error":"excution successfully completed"
    }


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)