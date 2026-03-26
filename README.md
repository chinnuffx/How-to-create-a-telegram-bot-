# 🤖 Telegram Bot Creation & Deployment Guide (Termux + Python)

This repository provides a **complete step-by-step guide** to create a Telegram bot using Python and run it on Termux (Android). Perfect for beginners who want to build and host bots directly from their phone.

---

## 📌 Features

* Create a Telegram bot using BotFather
* Python-based bot (easy to modify)
* Run bot on Android using Termux
* Beginner-friendly setup
* Fully customizable responses

---

## ⚙️ Requirements

Make sure you have:

* Android phone
* Internet connection
* Telegram account
* Termux app installed (from F-Droid recommended)

---

## 🚀 Step 1: Create Telegram Bot

1. Open Telegram
2. Search for **@BotFather**
3. Send:

   ```
   /start
   ```
4. Then:

   ```
   /newbot
   ```
5. Set:

   * Bot Name
   * Username (must end with `bot`)
6. Copy your **BOT TOKEN**

---

## 📲 Step 2: Install Termux & Setup Environment

Open Termux and run:

```bash
pkg update && pkg upgrade -y
pkg install python -y
pkg install git -y
pip install python-telegram-bot
```

---

## 📁 Step 3: Create Bot File

Create a Python file:

```bash
nano bot.py
```

Paste the following code:

```python
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Telegram bot 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
```

---

## 🔑 Step 4: Add Your Bot Token

Replace:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

With your actual token from BotFather.

---

## ▶️ Step 5: Run the Bot

Run the bot using:

```bash
python bot.py
```

If everything is correct, you’ll see:

```
Bot is running...
```

---

## 📡 Step 6: Test Your Bot

1. Open Telegram
2. Search your bot username
3. Click **Start**
4. Send messages and test responses

---

## 🔁 Auto Restart (Optional)

Install `tmux` to keep bot running:

```bash
pkg install tmux -y
tmux
python bot.py
```

Detach session:

```
CTRL + B then D
```

---

## 🧠 Customization Ideas

* Auto reply specific words
* Create spam bot
* Add commands (/help, /about)
* Connect APIs
* Build AI chat bot

---

## ⚠️ Common Errors

### ❌ Module not found

Run:

```bash
pip install python-telegram-bot
```

### ❌ Invalid Token

Check BOT TOKEN again

### ❌ Bot not responding

* Ensure script is running
* Check internet connection

---

## 📂 Project Structure

```
telegram-bot/
│── bot.py
│── README.md
```

---

## 💡 Tips

* Keep your token private
* Don’t stop Termux if bot is running
* Use tmux for background running

---

## 📜 License

This project is free to use and modify.

---

## ❤️ Support

If this helped you, consider starring ⭐ the repo.

---

## 👨‍💻 Author

**Poornesha Devadiga**

---
