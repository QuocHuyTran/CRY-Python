import requests

# crygo nonchart: xem tất cả coin nonchart
#crygo nonchart index: xem coin ở vị trí index
#crygo nonchart index full: xem đầy đủ giá trị ở coin vị trí index
#crygo nonchart coin: xem coin dựa theo symbol
# [{'name': 'DigiByte', 'symbol': 'DGB', 'available_supply': '10128477686.0', 'last_values': {'timeStamp': 1523991242, 'price': 0.0303954, 'marketcap': 307859131, 'volume24': '6232910.0', 'change_1h': '0.37', 'change_24h': '6.05'}}]


class CoinAPI:
    API_GET_COIN='http://cryws.herokuapp.com/api/coins/'
    API_GET_LIMIT_COIN='http://cryws.herokuapp.com/api/coins/offset/'

    API_GET_CHART_LIMIT_COIN='http://cryws.herokuapp.com/api/coins/chart7days/offset/'
    API_GET_CHART_COIN='http://cryws.herokuapp.com/api/coins/chart7days/'

    API_GET_COIN_NONCHART='http://cryws.herokuapp.com/api/coins/nonchart/'
    API_GET_LIMIT_COIN_NONCHART='http://cryws.herokuapp.com/api/coins/nonchart/offset/'

    API_CREATE_ACCOUNT='http://cryws.herokuapp.com/api/accounts/'
    API_LOGIN_ACCOUNT='http://cryws.herokuapp.com/api/accounts/login/'
    API_FAVORITE_ACCOUNT='http://cryws.herokuapp.com/api/accounts/favorites/'


def getAllNonchartCoin():
    coinAPI=CoinAPI()
    response=requests.get(coinAPI.API_GET_COIN_NONCHART);
    JSONArray=response.json()
    for index in range(len(JSONArray)):
        print(str(index)+"     "+JSONArray[index]['name']+"        "+JSONArray[index]['symbol']+"          "+"PRICE: "+str(JSONArray[index]['last_values']['price'])+"          "
              +"CHANGE 1H:"+str(JSONArray[index]['last_values']['change_1h'])+"         ")

def getNonchartCoin(symbol):
    coinAPI=CoinAPI()
    response = requests.get(coinAPI.API_GET_COIN_NONCHART+symbol);
    JSONArray = response.json()
    print(str(JSONArray[0]['name'] + "(" + JSONArray[0][
        'symbol'] + ")" + "          " + "PRICE: " + str(JSONArray[0]['last_values']['price']) + "          "
          + "CHANGE 1H:" + str(JSONArray[0]['last_values']['change_1h']) + "         " + "CHANGE_24H:" + str(
        JSONArray[0]['last_values']['change_24h'])))


def getNonchartCoinIndex(index,flag):
    coinAPI = CoinAPI()
    response = requests.get(coinAPI.API_GET_COIN_NONCHART);
    JSONArray = response.json()

    response=requests.get(coinAPI.API_GET_COIN_NONCHART+JSONArray[index]['symbol'])
    JSONArray=response.json()
    if(flag==1):
        print(str(index) + "    " + JSONArray[0]['name'] +"("+ JSONArray[0][
            'symbol']+")" + "          " + "PRICE: " + str(JSONArray[0]['last_values']['price']) + "          "
              + "CHANGE 1H:" + str(JSONArray[0]['last_values']['change_1h']) + "         "+"CHANGE_24H:"+str(JSONArray[0]['last_values']['change_24h']))
    else:
        print(str(index) + "      " + JSONArray[0]['name']+"(" + JSONArray[0][
            'symbol']+")" + "          " + "PRICE: " + str(JSONArray[0]['last_values']['price']) + "          "
              + "CHANGE 1H:" + str(JSONArray[0]['last_values']['change_1h']) + "         " +"CHANGE_24H:"+str(JSONArray[0]['last_values']['change_24h']))

        print("VOLUME24H:"+JSONArray[0]['last_values']['volume24']+"     "+"AVAILABLE_SUPPLY:"+str(JSONArray[0]['available_supply']+"      "+"MARKETCAP:"+str(JSONArray[0]['last_values']['marketcap'])))


def CreateAccount(username,password):
    coinAPI=CoinAPI()
    dataPost={'username':username ,'password':password}
    response=requests.post(coinAPI.API_CREATE_ACCOUNT,data=dataPost)
    print(response.json())

def LoginAccount(username,password):
    coinAPI=CoinAPI()
    dataPost = {'username': username, 'password': password}
    response = requests.post(coinAPI.API_LOGIN_ACCOUNT, data=dataPost)
    JSONObject=response.json()
    return JSONObject
    # print(JSONObject['token'])

def FavoriteCoin(token):
    coinAPI=CoinAPI()
    dataPost={}
    headerPost={'Authorization': token}
    response=requests.get(coinAPI.API_FAVORITE_ACCOUNT, headers={'Authorization': token})
    print(response.json())

def AddFavoriteCoin(token,symbol):
    coinAPI=CoinAPI()

    headerPost = {'Authorization': token}
    response = requests.post(coinAPI.API_FAVORITE_ACCOUNT, headers={'Authorization': token})

# print(LoginAccount("tqhuy","123"))
# LoginAccount("tqhuy","123")
def StartProgram():
    TOKEN=""
    print("Welcome to CRY")
    print("1:Sign In")
    print("2:Creat Account")
    s=input()
    if(s=='1'):
        print("username:")
        username=input()
        print("password")
        password=input()
        result=LoginAccount(username,password)['success']
        print(result)
        # TOKEN = LoginAccount(username, password)['token']
        if(result=="True"):
            while(True):
                print("1:Xem tất cả các coin nonchart")
                print("2:Xem Coin Chi Tiết")
                print("3:Xem Coin Chi Tiết Theo Index")
                choose = input()
                if (choose == "1"):
                    getAllNonchartCoin()
                elif (choose == "2"):
                    Symbol = input()
                    getNonchartCoin(Symbol)
                elif (choose == "3"):
                    Index = int(input())
                    print("1:")

        # if(TOKEN="?")
        else:
            print("Kết thúc")

StartProgram()
# getNonchartC1oinIndex(34,2)
# getNonchartCoin("BTC")
# CreateAccount('tqhuy','123')
# print(LoginAccount('tqhuy','123'))