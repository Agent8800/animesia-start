from pyrogram import Client, filters

# Replace with your bot token
API_TOKEN = "7033499587:AAE9ZC3gAetGvISzqFlzY8etuRmTYwCjfP8"

# Create a Pyrogram client
app = Client("animesia_bot", api_id=API_TOKEN, api_hash="YOUR_API_HASH")

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
app.run()￼Enter
