@bot.message_handler(func=lambda message: True)
def func_name(message):
	if message.text in array:
		import requests
		yahooql = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s') and u='c'" % message.text
		url = "https://query.yahooapis.com/v1/public/yql?q=%s&format=json" % yahooql
		r = requests.get(url)
		data = r.json()
		temp = data['query']['results']['channel']['item']['condition']['temp']
		bot.send_message(message.chat.id, "Today in Almety %s C" % temp, reply_markup = markup)