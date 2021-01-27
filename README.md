# [Telegram Bot Demo](https://suhail.pw)

Here is a working demo using backend url <https://suhail.pw>.

Open telegram app and search for bot **impress_ai_bot**:

![demo](https://raw.github.com/suhailvs/telegram_bot/main/telegram_bot.gif)


## Run locally

### 1. Clone the Repository

    git clone https://github.com/suhailvs/telegram_bot
    cd telegram_bot

create `.env` file and update `SECRET_KEY`:

    cp .env.example .env

### 2. Create virtualenv and install dependencies

	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt

### 3. Migrate database and Runserver

	./manage.py migrate
	./manage.py runserver

now visit <http://localhost:8000>

### 4. Setup your telegram bot

To create a chatbot on Telegram, you need to contact the [BotFather](https://telegram.me/BotFather).

Start telegram, and search for the Botfather. Type command `/newbot` to create a bot and follow the instructions to get a token:

![botfather](https://raw.github.com/suhailvs/telegram_bot/main/botfather.webp)

Your bot should have two attributes: a name and a username - which must end with "bot".

The token should look something like this: `2483457814:AAHrlCx234_VskzWEJdWjTsdfuwejHyu5mI`

In the **.env** file and update `TELEGRAM_TOKEN`:

	TELEGRAM_TOKEN=2483457814:AAHrlCx234_VskzWEJdWjTsdfuwejHyu5mI

### 5. Ngrok setup for HTTPS

To use telegram webhooks you need HTTPS url. You can use [ngrok](https://ngrok.com/). It gives a web-accessible HTTPS url that tunnels through to your localhost.

Download [ngrok](https://ngrok.com/). then on terminal run `./ngrok http 8000`. note down ngrok_url with https something like <https://0b5b17d6a644.ngrok.io>

### 6. Set your webhook by sending a post request to the Telegram API

run the following command in your terminal(replace ngrok_url and TELEGRAM_TOKEN)

	curl -F "url=<ngrok_url>/bot/" https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook


Now open your telegram app and open the bot and talk to it to get responses from it


## Run Tests

	./manage.py test --keepdb