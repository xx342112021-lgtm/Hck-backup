# TEAM AIMX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "39170545"
    API_HASH = "65959028b3bddfd808d52d0f93749bc0"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "8704597595:AAEGaCvoc8zI_UvC4YYfX5MOgxml5feFToA")
    MONGO_URL = "mongodb+srv://Che3434:Che3434@cluster0.oemtavn.mongodb.net/?appName=Cluster0"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["8109752681"])
