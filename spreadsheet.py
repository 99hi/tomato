import requests

#Googleスプレッドシートに追記
def ifttt_webhook(moi_per, temp, hum):
    payload = {"value1": moi_per,
                "value2": temp,
                "value3": hum
               }
    url = "https://maker.ifttt.com/trigger/temperature/with/key/dtnuJuewdgLt8U8HZfqR3c"
    requests.post(url, data=payload)
    print("シートに追加しました")