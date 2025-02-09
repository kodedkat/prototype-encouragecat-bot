import discord, random, datetime, encouraging_messages
from holiday_messages import holiday_messages_dict

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

def datetime_message():
    current_date = datetime.date.today()
    return holiday_messages_dict.get((current_date.month, current_date.day))
def random_message():
  return random.choice(encouraging_messages.encouraging_messages_list)
  
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$encat'):
        encouraging_message = random_message()
        holiday_message = datetime_message()

        if holiday_message:
          await message.channel.send(f'{encouraging_message}\n\n{holiday_message}')
        else:
          await message.channel.send(encouraging_message)

client = MyClient(intents=intents)
client.run('[ insert discord bot token here ]')
