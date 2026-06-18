# TEAM AIMX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20136640"
    API_HASH = "32fa482ffd34ceefec26b7ccd73c4fbb"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7997432877:AAFGm-u5Q56jZSIEw2nTmKcL_r0Cbu76hTk")
    MONGO_URL = "mongodb+srv://Che4721:Che4721@cluster0.88srl.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["8109752681"])
