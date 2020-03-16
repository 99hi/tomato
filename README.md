# ビニールハウスの環境管理
![tomatokousei](https://user-images.githubusercontent.com/61372460/75842073-c07c1100-5e12-11ea-9256-f636c7d0064e.jpg)
システム構成は上記になります。  
子機で温湿度、土壌水分量を測定し親機でデータを集めます。  
それからgooglespreadsheetに追記し、LINEにデータを送信します。 
これをcrontabで10分おきに実行させます。  
当初は無線での実装を考えていましたが、電池の交換で手間が掛かってしまうため  
有線で実装を行いました。  
現在はより効率的でコスト削減を重視した改良版を作成中です。  

※載せているコードはデモバージョンとして作成したものになります。  

## 使用したもの  
Raspberry Pi3 B+    
土壌水分量センサー: DFROBOT SEN0114    
温湿度センサー: BME280    

## 概要
温度と湿度、土壌水分量を取得し、googlespreadsheetに保存します。  
そして、いずれかが既定値を超えた場合にLINEに通知します。  
