import requests
import time
import telebot
from bs4 import BeautifulSoup

TOKEN = "INSERISCI_IL_TUO_TOKEN"
CHAT_ID = "INSERISCI_IL_TUO_CHAT_ID"
bot = telebot.TeleBot(TOKEN)

# Lista degli artisti e URL da monitorare
artists = [
    {"name": "Vasco Rossi", "urls": [
        "https://www.ticketone.it/event/vasco-rossi/",
        "https://www.ticketmaster.it/event/vasco-rossi/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Vasco-Rossi-Biglietti"
    ]},
    {"name": "Laura Pausini", "urls": [
        "https://www.ticketone.it/event/laura-pausini/",
        "https://www.ticketmaster.it/event/laura-pausini/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Laura-Pausini-Biglietti"
    ]},
    {"name": "Eros Ramazzotti", "urls": [
        "https://www.ticketone.it/event/eros-ramazzotti/",
        "https://www.ticketmaster.it/event/eros-ramazzotti/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Eros-Ramazzotti-Biglietti"
    ]},
    {"name": "Tiziano Ferro", "urls": [
        "https://www.ticketone.it/event/tiziano-ferro/",
        "https://www.ticketmaster.it/event/tiziano-ferro/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Tiziano-Ferro-Biglietti"
    ]},
    {"name": "Jovanotti", "urls": [
        "https://www.ticketone.it/event/jovanotti/",
        "https://www.ticketmaster.it/event/jovanotti/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Jovanotti-Biglietti"
    ]},
    {"name": "Måneskin", "urls": [
        "https://www.ticketone.it/event/maneskin/",
        "https://www.ticketmaster.it/event/maneskin/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Måneskin-Biglietti"
    ]},
    {"name": "Ed Sheeran", "urls": [
        "https://www.ticketone.it/event/ed-sheeran/",
        "https://www.ticketmaster.it/event/ed-sheeran/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Ed-Sheeran-Biglietti"
    ]},
    {"name": "The Weeknd", "urls": [
        "https://www.ticketone.it/event/the-weeknd/",
        "https://www.ticketmaster.it/event/the-weeknd/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/The-Weeknd-Biglietti"
    ]},
    {"name": "Adele", "urls": [
        "https://www.ticketone.it/event/adele/",
        "https://www.ticketmaster.it/event/adele/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Adele-Biglietti"
    ]},
    {"name": "Harry Styles", "urls": [
        "https://www.ticketone.it/event/harry-styles/",
        "https://www.ticketmaster.it/event/harry-styles/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Harry-Styles-Biglietti"
    ]},
    {"name": "Billie Eilish", "urls": [
        "https://www.ticketone.it/event/billie-eilish/",
        "https://www.ticketmaster.it/event/billie-eilish/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Billie-Eilish-Biglietti"
    ]},
    {"name": "Post Malone", "urls": [
        "https://www.ticketone.it/event/post-malone/",
        "https://www.ticketmaster.it/event/post-malone/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Post-Malone-Biglietti"
    ]},
    {"name": "Coldplay", "urls": [
        "https://www.ticketone.it/event/coldplay/",
        "https://www.ticketmaster.it/event/coldplay/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Coldplay-Biglietti"
    ]},
    {"name": "Bruce Springsteen", "urls": [
        "https://www.ticketone.it/event/bruce-springsteen/",
        "https://www.ticketmaster.it/event/bruce-springsteen/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Bruce-Springsteen-Biglietti"
    ]},
    {"name": "Metallica", "urls": [
        "https://www.ticketone.it/event/metallica/",
        "https://www.ticketmaster.it/event/metallica/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Metallica-Biglietti"
    ]},
    {"name": "Maroon 5", "urls": [
        "https://www.ticketone.it/event/maroon-5/",
        "https://www.ticketmaster.it/event/maroon-5/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Maroon-5-Biglietti"
    ]},
    {"name": "Shawn Mendes", "urls": [
        "https://www.ticketone.it/event/shawn-mendes/",
        "https://www.ticketmaster.it/event/shawn-mendes/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Shawn-Mendes-Biglietti"
    ]},
    {"name": "One Direction", "urls": [
        "https://www.ticketone.it/event/one-direction/",
        "https://www.ticketmaster.it/event/one-direction/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/One-Direction-Biglietti"
    ]},
    {"name": "Sam Smith", "urls": [
        "https://www.ticketone.it/event/sam-smith/",
        "https://www.ticketmaster.it/event/sam-smith/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Sam-Smith-Biglietti"
    ]},
    {"name": "Rihanna", "urls": [
        "https://www.ticketone.it/event/rihanna/",
        "https://www.ticketmaster.it/event/rihanna/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Rihanna-Biglietti"
    ]},
    {"name": "Drake", "urls": [
        "https://www.ticketone.it/event/drake/",
        "https://www.ticketmaster.it/event/drake/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Drake-Biglietti"
    ]},
    {"name": "Travis Scott", "urls": [
        "https://www.ticketone.it/event/travis-scott/",
        "https://www.ticketmaster.it/event/travis-scott/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Travis-Scott-Biglietti"
    ]},
    {"name": "Kendrick Lamar", "urls": [
        "https://www.ticketone.it/event/kendrick-lamar/",
        "https://www.ticketmaster.it/event/kendrick-lamar/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Kendrick-Lamar-Biglietti"
    ]},
    {"name": "Imagine Dragons", "urls": [
        "https://www.ticketone.it/event/imagine-dragons/",
        "https://www.ticketmaster.it/event/imagine-dragons/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Imagine-Dragons-Biglietti"
    ]},
    {"name": "Nicki Minaj", "urls": [
        "https://www.ticketone.it/event/nicki-minaj/",
        "https://www.ticketmaster.it/event/nicki-minaj/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Nicki-Minaj-Biglietti"
    ]},
    {"name": "Cardi B", "urls": [
        "https://www.ticketone.it/event/cardi-b/",
        "https://www.ticketmaster.it/event/cardi-b/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Cardi-B-Biglietti"
    ]},
    {"name": "The Rolling Stones", "urls": [
        "https://www.ticketone.it/event/rolling-stones/",
        "https://www.ticketmaster.it/event/rolling-stones/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/The-Rolling-Stones-Biglietti"
    ]},
    {"name": "Lizzo", "urls": [
        "https://www.ticketone.it/event/lizzo/",
        "https://www.ticketmaster.it/event/lizzo/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/Lizzo-Biglietti"
    ]},
    {"name": "P!nk", "urls": [
        "https://www.ticketone.it/event/pink/",
        "https://www.ticketmaster.it/event/pink/",
        "https://www.viagogo.it/Eventi-Music/Concerti/Artisti/P!nk-Biglietti"
    ]}
]

def check_availability(artist):
    for url in artist["urls"]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Verifica disponibilità biglietti
        if "Sold Out" not in soup.text:
            message = f"🎟️ Biglietto DISPONIBILE per {artist['name']}! Compra ora: {url}"
            bot.send_message(CHAT_ID, message)

while True:
    for artist in artists:
        check_availability(artist)
    time.sleep(300)  # Controlla ogni 5 minuti
