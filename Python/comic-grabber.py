"""
This was created as a friend and myself thought this person's comics were
very strange and funny
Currently this is running as a cronjob on my server
"""
from discord_webhook import DiscordWebhook
from lxml import html
import requests
import datetime

def get_image_link():
    """
    Goes to the website that hosts his comics
    Then gets the HTML and looks for the link for the image
    """
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    headers = {"User-Agent": user_agent}
    date = datetime.datetime.now()
    date_str = date.strftime("%Y/%m/%d")
    url = f"https://www.gocomics.com/heathcliff/{date_str}"
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    image = tree.xpath('//meta[@property="og:image"]/@content')
    return image[0].strip()

def push_to_discord(link: str):
    """
    Posts the link to the specified discord webhook
    """
    webhook = DiscordWebhook("<your_webhook_link>", content = link)
    webhook.execute()

if __name__ == "__main__":
    log = open("comic-grabber.log", "a")
    log.write(f"{datetime.datetime.now().strftime('%Y/%m/%d - %I:%M:%S %p')} >> Begin comic grab\n")
    link = get_image_link()
    log.write(f"{datetime.datetime.now().strftime('%Y/%m/%d - %I:%M:%S %p')} >> Image link found, {link}\n")
    push_to_discord(link)
    log.write(f"{datetime.datetime.now().strftime('%Y/%m/%d - %I:%M:%S %p')} >> Pushed to Discord\n")
    log.close()