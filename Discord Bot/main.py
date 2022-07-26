import discord
import os
import utils

TOKEN = "xxx"

# connects to discord websocket and api
client = discord.Client()

# called when bot is online
@client.event
async def on_ready():
  print(f"{client.user} is online.")

# called on message
@client.event
async def on_message(message):
  
  # if bot (self) said something, ignore
  if message.author == client.user:
    return

  # command initializer
  if message.content.lower().startswith("!s"):

    # assigning general variables for log
    user_name = str(message.author).split('#')[0]
    user_message = str(message.content)
    msg_channel = str(message.channel.name)
    # command log
    print(f"{user_name}: {user_message} (#{msg_channel})")

    # assigning command to variable
    command = str(message.content[2:])
    
    # !sithVote command
    if command.lower() == "ithvote":

      if message.channel.id == 986537383250001940:
        # response message
        vote_msg = await message.channel.send("Starting vote!\nReact with ✅ to vote yes, ❌ to vote no, and ⭕ to abstain from the vote.\nPlease vote only ONE time!")
        yes_vote = "✅"
        no_vote = "❌"
        abstain = "⭕"
        await vote_msg.add_reaction(yes_vote)
        await vote_msg.add_reaction(no_vote)
        await vote_msg.add_reaction(abstain)
        # log
        print("Command executed successfully.\n")

      else:
        # incorrect channel error for log
        await message.channel.send("Incorrect channel. Resubmit command in #votes channel.")
        print("Error: incorrect channel.\n")
        return

    else:
      # unknown command error for log
      await message.channel.send("Unknown command.")
      print("Error: unknown command.\n")

  if message.content.lower() == "fuck you parry":
    await message.channel.send("Yeah, fuck you Parry!")

# start bot
client.run(TOKEN)
