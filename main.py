import frenchcord
client = frenchcord.Robot('bot_token')
@client.event('en_marche')
def say_online():
  print('online!')
 
@client.command
def hello(ctx):
  ctx.salon.envoyer('Salut')

client.connexion('?')
