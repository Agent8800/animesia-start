from pyrogram import Client, filters

# Replace with your bot token
BOT_TOKEN = "7033499587:AAE9ZC3gAetGvISzqFlzY8etuRmTYwCjfP8"

# Replace with your API ID
API_ID = "7391573"

# Replace with your API hash
API_HASH = "1f20df54dfd91bcee05278d3b01da2c7"

# Create a Pyrogram client
app = Client("animesia_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define a filter for the start command
start_filter = filters.command("start")

# Define a function to handle the start command
@app.on_message(start_filter)
async def start_message(client, message):
    # Stylish entry message
    text = f"**Welcome to Animesia App Bot!**\n\n"
    text += "Explore the world of anime with us!\n"
    text += "[Download App](https://example.com/animesia_app) | [Channel Updates](https://t.me/animesia_update)\n"
    text += "Developed by [Majid](https://t.me/dev_username) | Admin: [Kirito](https://t.me/dou_di_emperor)"

    # Send an image or video with the message
    media = "animesia_image.jpg"  # Replace with your image or video file
    await message.reply_photo(media, caption=text, parse_mode="markdown")

    # Alternatively, you can send a video using send_video
    # media = "animesia_video.mp4"
    # await message.reply_video(media, caption=text, parse_mode="markdown")

# Run the bot
if __name__ == "__main__":
    app.run()
