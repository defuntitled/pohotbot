from discord.ext import commands
import asyncio
import requests

TOKEN = "NzA2MzYwOTYzOTU5NDg4NTU1.Xq-lrQ.kSRe041t0kflksPGoqDoeD3wVLw"
city = "Barnaul"
key = "a6e3d155c190199497d700ebe6784302"


class Brain(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='timer')
    async def roll_dice(self, ctx, count):
        try:
            time = count.split(":")
            hours = int(time[0])
            minutes = int(time[1])
            sec = int(time[2])
            minutes += hours * 60
            sec += minutes * 60
            author = ctx.message.author
            await ctx.send(author.mention + "timer set")
            await asyncio.sleep(sec)
            await ctx.send(author.mention + "TIME OUT!!!!!!!!!")
        except (ValueError, IndexError):
            await ctx.send("Incorrect delay")

    @commands.command(name="pasta")
    async def pasta(self, ctx, board):
        try:
            pasta = requests.get(f"https://2ch.hk/{board}/index.json").json()
            pasta = pasta["threads"][0]["posts"][0]
            try:
                media = pasta["files"][0]["path"]
                await ctx.send(pasta["comment"] + " " + "https://2ch.hk" + media)
            except (KeyError, IndexError):
                await ctx.send(pasta)
        except:
            await ctx.send("sorry 2ch api govno")

    @commands.command(name="help_bot")
    async def help(self, ctx):
        await ctx.send(
            "prefix - $\ntimer <h : m : s>\npasta <board_name>\nplace - place " +
            "for weather\ncurrent - current weather\nforecast - weather for n days")

    @commands.command(name="place")
    async def place(self, ctx, place):
        global city
        city = place
        await ctx.send("city changed successful")

    @commands.command(name="current")
    async def current(self, ctx):
        global key, city
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}").json()
        await ctx.send(
            f"temp: {int(weather['main']['temp']) - 273.0}\n{weather['weather'][0]['description']}\n" +
            f"wind speed:{weather['wind']['speed']} mps")

    @commands.command(name="forecast")
    async def forecast(self, ctx, days):
        global key, city
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": city,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]['Point']['pos'].split()
        params = {'lat': toponym[1],
                  'lon': toponym[0],
                  'lang': 'en_US',
                  'limit': days}
        head = {"X-Yandex-API-Key": '6558babd-c5bf-4bd4-9cee-6d0482b98301'}

        forecast = requests.get("https://api.weather.yandex.ru/v1/informers/", params=params,
                                headers=head).json()
        await ctx.send(f"max " +
                       f"temp:{forecast['forecast']['parts'][0]['temp_max']}\nmin" +
                       f" temp:{forecast['forecast']['parts'][0]['temp_min']}\n" +
                       f"{forecast['forecast']['parts'][0]['condition']}")


bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("готов вкалывать")


bot.add_cog(Brain(bot=bot))
bot.run(TOKEN)
