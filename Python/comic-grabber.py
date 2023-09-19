"""
This was created as a friend and myself thought this person's comics were
very strange and funny, so I decided to quickly write this
I do not use discord much but I thought this was funny enough to make
Just uses html requests to get the image link and then uses the discord
webhook library to post to discord
Currently this is running as a cronjob on my server
"""
from discord_webhook import DiscordWebhook
from lxml import html, etree
import requests
import re

def get_image_link():
	"""
	Goes to the website that hosts his comics
	Then gets the HTML and looks for the link for the image
	"""
	page = requests.get("https://www.creators.com/read/heathcliff")
	tree = html.fromstring(page.content)
	image = etree.tostring((tree.xpath('//*[@id="comedy-show-banner"]/a/img'))[0])
	link = re.findall("http[s]*\S+", image.decode('utf-8'))
	return link[0].strip("\"")

def push_to_discord(link: str):
	"""
	Posts the link to the specified discord webhook
	"""
	webhook = DiscordWebhook("<your_webhook_link>", content = link)
	webhook.execute()

if __name__ == "__main__":
	link = get_image_link()
	push_to_discord(link)