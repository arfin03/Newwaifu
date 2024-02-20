class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6649432492"
    sudo_users = "6649432492", "5843270062", "1495261563", "6489025882"
    GROUP_ID = -1002015833205
    TOKEN = "6961758741:AAFjH5DEI1jiDJUG9WFEqv5hpdkDYvzaN8A"
    mongo_url = "mongodb+srv://arfin01:Arkaku123@cluster0.s2drx4p.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/1319554970a8697738eb3.jpg", "https://telegra.ph/file/33298b6daefbd0e3a20f4.jpg"]
    SUPPORT_CHAT = "gcanimecommunity"
    UPDATE_CHAT = "Origanimeinfo"
    BOT_USERNAME = "Guess_wwaifu_bot"
    CHARA_CHANNEL_ID = "-1002124487227"
    api_id = 17204044
    api_hash = "db2dd5d8401971aa433ef3c0f9a108da"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
