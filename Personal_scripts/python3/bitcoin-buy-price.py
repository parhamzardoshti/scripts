import requests

def inform_parham(res):
    API_KEY  = '786C47476F7356797A56425A6862665670374D73425469786A306277676B79546F6D4A7557627964396F413D'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json'% API_KEY
    payload = {'receptor': '09912093224' , 'message':'price is %i DOLLAR ' %res}
    requests.post(url , data=payload )
    print("the price is %i $" %(res))
    print("see that! its actually")

good_price = 8500
    
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD' , proxies={'http':'socks5://127.0.0.1:9050'})
res =float(response.json()['data']['amount'])

if (good_price < res):

    inform_parham(res)


