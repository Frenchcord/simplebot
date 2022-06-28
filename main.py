import frenchcord
client = frenchcord.Robot('bot_token')
@client.event('on_ready')
def say_online():
  print('online!')

@client.event('message')
def cmd(message):
  if message.author.id == client.me.id: return
  client.process_commands(message) 
 
@client.command
def hello(ctx):
  ctx.salon.envoyer('Salut')

client.connexion('?')
