#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .
from decouple import config

# For Local deployment uncomment the commented variables and comment the
# uncommented ines


try:
    APP_ID = config("APP_ID", "4018758")
    # APP_ID = ""
    API_HASH = config("API_HASH", "622bba3cf046315531f71f9d97fa6c2a")
    # API_HASH = ""
    BOT_TOKEN = config("BOT_TOKEN", "5822396703:AAH2V7eOy9-UdqyVpWkawnHbDXzdvpfsc0w")
    # BOT_TOKEN = ""
    DEV = 5385471287
    OWNER = config("OWNER", "5385471287")
    # OWNER = ""
    FFMPEG = config("FFMPEG", "ffmpeg -i '''{}''' -c:v libx265 -crf 28 -c:s copy? -s 854x480 -preset veryfast -ab 35k '''{}''' -y")
    #FFMPEG = 
    THUMB = config("THUMBNAIL", "https://telegra.ph/file/ab23f5209aae9cae3bac.jpg")
    # THUMB = ""
    ICON = config("ICON", "https://te.legra.ph/file/462b5a002f80bdf8a1ec1.png")
    # ICON = ""
    LOG_CHANNEL = config("LOG_CHANNEL", "-1001533601450")
    # LOG_CHANNEL = ""
    DBNAME = config("DBNAME", "TgEncode")
    # DBNAME = ""
    DATABASE_URL = config("DATABASE_URL", "mongodb+srv://Nikhil:lol@cluster0.opa09.mongodb.net/?retryWrites=true&w=majority")
    # DATABASE_URL = ""
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
