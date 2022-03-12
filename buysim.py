import requests
import time

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzgyNzcxODMsImlhdCI6MTY0Njc0MTE4MywicmF5IjoiMGY1NzJhZTEyODljZDhmOTc0ODM3NDI3YjgzZGIwODIiLCJzdWIiOjk3NDU1OX0.ZlD3W-QPrQyv995m721dPrI3lfKQoY9zlRQ5laJABQVEDDNHP-MM3JQ94RWqCuDY24htMPEn3ahXCtrR31A68xzkObvrwzim75oBVgJDVqLrkwrOlBOfH6IvYKp3bhIhX35Tg0LCvO6RKhQv-09rYdILxfpCBF_EKGlOwBkzsOrm0BXI2NE5crp_Id5NegT3T_mezX89YQybYvGITms5UMSaOy9PwKxNVABIH7-omKBMLOtsNTahedRg5PwMBrTIx9uwWtLig5-GAX7K08auiQATQeYOmooRLrLKVJaHlDphrYDX7kimnxnmbdIieJ0RqNZ6kfgBsrmGViZBkODy9A'

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}
def buy_google_number():
    while True:
        time.sleep(1)
        try:
            response = requests.get('https://5sim.net/v1/user/buy/activation/usa/any/google', headers=headers)
            response = response.json()
            print("buycell:", response)
            return response
        except Exception as e:
            pass
def get_sms(serviceid):
    response = requests.get('https://5sim.net/v1/user/check/'+str(serviceid), headers=headers)
    response = response.json()
    return response
def ban_order(serviceid):
    response = requests.get('https://5sim.net/v1/user/ban/'+str(serviceid), headers=headers)
    print(response)
    return
def cancel_order(serviceid):
    response = requests.get('https://5sim.net/v1/user/cancel/'+str(serviceid), headers=headers)
    print(response)

    return 
def finish_order(serviceid):
    response = requests.get('https://5sim.net/v1/user/finish/'+str(serviceid), headers=headers)
    print(response)

    return