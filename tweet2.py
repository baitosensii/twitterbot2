import tweepy
import time 
import random
import datetime 
import pandas as pd



CONSUMER_KEY="zlY7seK5dE83G1WMwr2EiXIYw"
CONSUMER_SECRET="csWTb7bEs621qndziYszaNZggCwwlMP52UqIICdzSDUOG6mqCw"
ACCESS_TOKEN="1454903800188178437-CYzg3fNjO7TahUkw9eQWbkDqizJXzA"
ACCESS_SECRET="6OvyNvXm8ZjMwlrLnaIFCSW7i1l19sTbjZcO6SDdTZjgF"

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api=tweepy.API(auth)

#トレンド取得
woeid = 23424856
trends = api.get_place_trends(woeid)
df = pd.DataFrame(trends[0]["trends"])

#画像用意
number=[0,1]
w=[500,1]
Img=["ピカチュウ.png","ビッパ.jpg"]

#日付時刻取得
dt_now = datetime.datetime.now()

#フォロバ
follower_id = api.get_follower_ids()
#follow_id = api.get_friend_ids()
#not_followed_user_id = set(follower_id) ^ set(follow_id)

#twitter　本文
message="現在は"+str(dt_now.year)+"年"+str(dt_now.month)+"月"\
    +str(dt_now.day)+"日"+str(dt_now.hour)+"時"\
    +str(dt_now.minute)+"分です。\n"+"\n"\
    +"現在の日本のtwitterトレンド上位5位↓\n"\
    +"1."+df.name[0]+"\n"\
    +"2."+df.name[1]+"\n"\
    +"3."+df.name[2]+"\n"\
    +"4."+df.name[3]+"\n"\
    +"5."+df.name[4]+"\n"+"\n"\
    +"画像は基本ピカチュウ、ごく稀にビッパが出てきます。"+"\n"\
    #+"※フォロバはツイートのタイミングで自動でします。"
    

abc=random.choices(number,weights=w)
image1=Img[abc[0]]
api.update_status_with_media(status=message,filename=image1)
   
for f in follower_id:
    api.create_friendship(f.ids)
    time.sleep(random.randrange(10))