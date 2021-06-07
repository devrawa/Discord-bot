import websockets
import discord
from discord.ext import commands
from discord import reaction
from discord import user

from discord.ext.commands import Bot   
bot = commands.Bot(command_prefix ='!')


    
    
    

@bot.event      
async def on_message(message):
    messageText = message.content
    if message.author == bot.user:
        return
    
    
    if message.content.startswith('!hello'):
        await message.channel.send('Salutare {}'.format(message.author)) 
        
    
    if '@everyone' in message.content:
        if "Lider" in [y.name.lower() for y in message.author.roles]:
            return
        else:    
            await message.delete()
            await message.channel.send('@{}, nu mai da everyone sau here'.format(message.author));   
        
    if '@here' in message.content:
        await message.delete()
        await message.channel.send('@{}, nu mai da everyone sau here'.format(message.author));   
        

@bot.event
async def on_ready():
    print("The bot is ready!")
    name = "Oversees the discord server"
    await bot.change_presence(status=discord.Status.online, activity = discord.Game(name))
  



@commands.command()
async def clear(ctx, number = '0'):
    if(number == '0'):
       await ctx.send('SyntaxError! The command usage is !clear x, where x is an unsigned int');    
    elif(int(number) < 0): 
       await ctx.send('SyntaxError! The command usage is !clear x, where x is an unsigned int');   
    else:       
        msg = []
        async for elem in ctx.history(int(number)):
               await ctx.send(msg);
               msg.append(elem)
               
        if(size(msg) >= 1):       
           await ctx.delete_messages(msg)
        else:
           await ctx.send('No message founded');    
    
bot.add_command(clear)

bot.run(Nzc5MDQ2MDUzODc3Nzc2NDI0.X7a1LQ.XRPbrNZN8VokA_nEus840Gdmfu0)
