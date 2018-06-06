# -*- coding: utf-8 -*-

@bot.inline_handler(lambda query: len(query.query))
def queryi_text(query):
  if query.query:
   try:
    oo = query.query
    input = oo.replace("music ","")
    text = input.replace(" ","-")
    jdat = requests.get('http://api.mostafa-am.ir/radio-javan/{}'.format(text)).json()
    imusics = []
    i = 0
    sr = jdat['Musics']
    for all in sr:
      ax = all['Photo']
      link = all['Url']
      ar = all['Artist']
      so = all['Song']
      i+= 1
      imusics.append(types.InlineQueryResultAudio(str(i), all['Url'], '🎙{}(@SPeedStarBot)'.format(all['Title']),caption='🎙 {}\n🎵 {}\n🆔 @SpeedStarBot'.format(all['Artist'],all['Song']))) 
    bot.answer_inline_query(query.id, imusics, cache_time="15")
   except:
    l = 'https://api.telegram.org/file/bot426931655:AAEKNE1cJQBPWr3wBdQFqlrr7Wr5Fq_6aw8/voice/505426782116409769.oga'
    s = types.InlineQueryResultVoice('1', l, 'دوباره امتحان کن🚫',caption='hi :)')
    bot.answer_inline_query(query.id, [s], cache_time="5")
