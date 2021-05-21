from decouple import config

TOKEN = config('TOKEN', default="", cast=str)
URL = 'https://api.notion.com/v1/'
