class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6649432492"
    sudo_users = "6649432492", "5008662958", "7127913934", "5843270062", "1495261563", "6489025882", "6752263178"
    GROUP_ID = -1002015833205
    TOKEN = "6872064337:AAGyofMcK81eno1XLCTG2f4LeRf9FacB-5Y"
    mongo_url = "mongodb+srv://Arfin:Arfin@cluster0.ynbtqna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/3c876536b6e57ed8bf5bb.jpg", "https://telegra.ph/file/d4f4d52d126fc95fbe312.jpg"]
    SUPPORT_CHAT = "gcanimecommunity"
    UPDATE_CHAT = "guess_update"
    BOT_USERNAME = "Take_waifu_bot"
    CHARA_CHANNEL_ID = "-1002118604770"
    api_id = 17204044
    api_hash = "db2dd5d8401971aa433ef3c0f9a108da"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
