import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.plugins.modules.blast import effect_markup

# Animation code (similar to your provided code)
def generate_animation(effect):
  animation_frames = []
  effect = random.choice(["flowers", "rockets", "rain", "leaves", "snow", "bombs"]) 
 
    # Create the animation 
  if effect == "flowers": 
        animation = [ 
            {"x": 0, "y": 0, "duration": 1}, 
            {"x": 100, "y": 0, "duration": 2}, 
            {"x": 0, "y": 100, "duration": 3}, 
            {"x": 100, "y": 100, "duration": 4}, 
        ] 
  elif effect == "rockets": 
        animation = [ 
            {"x": 0, "y": 0, "duration": 1}, 
            {"x": 100, "y": 0, "duration": 2}, 
            {"x": 200, "y": 0, "duration": 3}, 
            {"x": 300, "y": 0, "duration": 4}, 
            {"x": 300, "y": 100, "duration": 5}, 
            {"x": 200, "y": 200, "duration": 6}, 
            {"x": 100, "y": 300, "duration": 7}, 
            {"x": 0, "y": 400, "duration": 8}, 
        ] 
  elif effect == "rain": 
        animation = [ 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
        ] * 100 
  elif effect == "leaves": 
        animation = [ 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
        ] * 100 
  elif effect == "snow": 
        animation = [ 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
        ] * 100 
  elif effect == "bombs": 
        animation = [ 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
            {"x": random.randint(0, 100), "y": random.randint(0, 100), "duration": 1}, 
        ]
    return animation_frames

# Command to start the bot
@app.on_message(filters.command("magic"))
def magic(client, message):
  markup = effect_markup()
  msg = "Try these effects!"
  message.reply_text(msg, reply_markup=markup)

# Callback function for button clicks
@app.on_callback_query()
def button_click(client, callback_query):    
    effect = callback_query.data
    animation_frames = generate_animation(effect)

    # Send animation frames to the user
    for frame in animation_frames:
        client.send_animation(          
          animation=frame,
          width=100,  # Adjust width as needed
          height=100,  # Adjust height as needed
          duration=frame["duration"]  # Adjust duration from animation frame
        )
  
