#main
import temp_hum
import moisture
import line
import spreadsheet

tempmax = 30
hummax = 80
moimax = 30

def main():
    temp, hum = temp_hum.readData() #温度、湿度
    moi, moi_per = moisture.getval() #水分量、水分量(%)
    
    print("温度：" + str(temp) + "℃")
    print("湿度：" + str(hum) + "℃")
    print("水分量：" + str(moi))
    print("水分量：" + str(moi_per) + "%")
    
    #スプレッドシートに追加
    spreadsheet.ifttt_webhook(moi_per, temp, hum)
    
    #異常値だった注意文の追加
    value2 = ""
    if (temp > tempmax):
        value2 += "・ハウスが暑くなっています"
    
    if (hum > hummax):
        value2 += "・湿度が高くなっています"
        
    if (moi_per < moimax):
        value2 += "・水が不足しています"
    
    #異常値がない場合LINEは送らない
    if (value2 != ""):
        line.send_line(value2, temp, hum, moi_per)
        
        



if __name__ == '__main__':
    main()