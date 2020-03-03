import datetime
import requests


#LINEを送る
def send_line(value2, temp, hum, moi_per):
    payload = {"value1": datetime.datetime.now().strftime('%m月%d日 %H:%M'),
                "value2": value2,
                "value3": "温度：" + str(temp) + "℃\r\n" + "湿度：" + str(hum) + "％\r\n" + "土壌水分量：" + str(moi_per) + "％"
                }
    url = "https://maker.ifttt.com/trigger/line_event/with/key/dtnuJuewdgLt8U8HZfqR3c"
    requests.post(url, data=payload)
    print("LINEを送信しました")
