# -*- coding: utf-8 -*-
@bot.message_handler(func=lambda m: m.text.startswith("اذان"))
def getazan(m):
 try:
       fl = json.loads(urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(m.text.replace('اذان ',''))).read())
       lat = fl["results"][0]["geometry"]["location"]["lat"]
       lon = fl["results"][0]["geometry"]["location"]["lng"]
       time = jdatetime.datetime.now().strftime("%H:%M:%S")
       date = jdatetime.datetime.now().strftime("%Y/%m/%d")
       url = "http://api.aladhan.com/timings/{}?latitude={}&longitude={}&timezonestring=Asia/Tehran&method=7".format(time,lat,lon)
       i = json.loads(urllib.urlopen(url).read())
       data = i["data"]["timings"]
       city = m.text.replace('اذان ','')
       text = """
اوقات شرعی به افق _{}_
{}

🏙 اذان صبح:  {}
🌄 طلوع آفتاب:  {}
🌞 اذان ظهر:  {}
🌇 غروب خورشید:  {}
🌆 اذان مغرب:  {}
🌃 نیمه شب شرعی:  {}

""".format(city,dates(),data["Fajr"],data["Sunrise"],data["Dhuhr"],data["Sunset"],data["Maghrib"],data["Isha"],data["Midnight"])
       bot.reply_to(m,text,parse_mode="markdown")
 except:
   bot.reply_to(m,'دوباره امتحان کنید')
