import requests
import time
import random
from random import getrandbits
import names

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "           Fuck Who You Know              ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "          Developed by @mxnnxt            ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------\n")

times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of accounts you would like: ")))
domain = input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter your domain (ex: domain.com): "))

headers = {
    'Referer': 'https://www.johnelliott.co/pages/lebron-james-x-john-elliott-nikelab-icon-friends-family-giveaway',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

def submit():
	global session
	name = names.get_first_name()
	email = (name + "{}" + "@"+domain).format(getrandbits(40))
	sizes = ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","14","15"]
	size = sizes[random.randint(0, 14)]
	params = (
    ('u', 'b0d3e1fe6af1cb8dbeeb1c333'),
    ('id', '6f82135082'),
    ('c', 'jQuery31109362504305456354_1533690953997'),
    ('EMAIL', email),
    ('SHOESIZE', size),
    ('b_b0d3e1fe6af1cb8dbeeb1c333_6f82135082', ''),
    ('_', '1533690953998'),
	)

	response = requests.get('https://johnelliott.us16.list-manage.com/subscribe/post-json', headers=headers, params=params)
	print(response.text+" - "+email)



for i in range(times):
	submit()
