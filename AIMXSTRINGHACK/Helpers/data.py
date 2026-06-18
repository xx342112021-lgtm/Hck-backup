from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
** 𝐌𝐄𝐑𝐇𝐀𝐁𝐀 {},**
𝐁𝐄𝐍 **{}**, 𝐇𝐄𝐒𝐀𝐏 𝐄𝐋𝐄 𝐆𝐄𝐂̧𝐈̇𝐑𝐌𝐄 (𝐇𝐀𝐂𝐊) 𝐁𝐎𝐓𝐔𝐘𝐔𝐌.

Hem Pyrogram hem de Telethon string session yapılarını destekliyorum.
Neler yapabildiğimi görmek için hack butonuna tıkla.
"""

HACK_TEXT = """
"A" :~ [Kullanıcının kendi gruplarını ve kanallarını kontrol et]

"B" :~ [Telefon numarası, kullanıcı adı vb. tüm kullanıcı bilgilerini kontrol et]

"C" :~ [Bir grubu banla {StringSession ve kanal/grup kullanıcı adını ver, tüm üyeleri banlayayım}]

"D" :~ [Kullanıcının son OTP kodunu öğren {Önce B seçeneğiyle numara alıp giriş yapın, sonra bunu kullanın}]

"E" :~ [StringSession aracılığıyla bir Gruba/Kanala katıl]

"F" :~ [StringSession aracılığıyla bir Gruptan/Kanaldan ayrıl]

"G" :~ [Bir Grubu/Kanalı sil]

"H" :~ [İki adımlı doğrulamanın açık mı kapalı mı olduğunu kontrol et]

"I" :~ [Kendi StringSession'ın hariç tüm aktif oturumları sonlandır]

"J" :~ [Hesabı sil]

"K" :~ [Bir grupta/kanalda üyeyi yetkili yap]

"L" :~ [Bir gruptaki/kanaldaki tüm yöneticilerin yetkisini al]
"""

info = """
 ❥︎ İSİM : {}
 ❥︎ ID : {}
 ❥︎ TELEFON NO : +{}
 ❥︎ KULLANICI ADI : @{}
"""

# Buton metni Türkçe yapıldı, callback_data aynı bırakıldı
PM_BUTTON = IKM([[IKB("•─╼⃝𖠁 𝐇𝐀𝐂𝐊 𝐌𝐄𝐍𝐔̈𝐒𝐔̈ 𖠁⃝╾─•", callback_data="hack_btn")]])

HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),           
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
                    
    ],
    [
        IKB("J", callback_data="J"),
        IKB("K", callback_data="K"),
        IKB("L", callback_data ="L"),                            
    ],
    ],    
    )

LOG_TEXT = """
      ● HACK SESSION BOTU ●

 ❥︎ Pyrogram veya Telethon string session kullanarak
 ❥︎ Herhangi bir hesabı yönetmek için tasarlanmış bot.
 ❥︎ SAHİP : che
"""
