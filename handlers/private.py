from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/9190514dd95bb720fefa2.jpg",
                caption=(f"""⇨ **Merhaba Hoş Geldin [Efendim](tg://settings)** \n\n⇨ **Ben** {bot} \n\n⇨ **Sesli Sohbetlerde Müzik Çalabilirim** \n\n **Beni Gruba Yönetici olarak Ekleyip Kesintisiz Müziğin Tadını Çıkarabilirsiniz.**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Beni Gruba Ekle 🎉", url=f"https://t.me/MajesteMusicProBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 Asistan", url="https://t.me/MajesteMusicProAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 Sahibim", url="https://t.me/MacroPem"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 Sohbet Grubu", url=f"https://t.me/MajesteSohbetTr"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" Not ⇒ \n\n **Botun Aktif Çalışabilmesi için Şu 3 Yetkiye ihtiyacı vardır** ⇒ \n\n ⇒ **Sesli Sohbetleri Yönetme , Bağlantılar ile davet etme , Mesajları Silme** \n\n **bu 3 yetkiyi vererek botu kullanabilirsiniz**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📚 Tüm Komutlar", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "🗯️ Ana Menü ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "📩 Sahibim", url="https://t.me/MacroPem")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("Not ⇒ \n\n **Botun Aktif Çalışabilmesi için Şu 3 Yetkiye ihtiyacı vardır** ⇒ \n\n ⇒ **Sesli Sohbetleri Yönetme , Bağlantılar ile davet etme , Mesajları Silme** \n\n **bu 3 yetkiyi vererek botu kullanabilirsiniz**", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "📚 Tüm Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🗯️ Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "📩 Sahibim", url="https://t.me/MacroPem")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nsᴇsʟɪ sᴏʜʙᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ \n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📩 Sohbet Grubu", url="https://t.me/MajesteSohbetTr")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/MacroPem")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""⇨ **Merhaba Hoş Geldin [Efendim](tg://settings)** \n\n⇨ **Ben** {bot} \n\n⇨ **Sesli Sohbetlerde Müzik Çalabilirim** \n\n **Beni Gruba Yönetici olarak Ekleyip Kesintisiz Müziğin Tadını Çıkarabilirsiniz.**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝐁𝐞𝐧𝐢 𝐆𝐫𝐮𝐛𝐚 𝐄𝐤𝐥𝐞 🎉", url=f"https://t.me/MajesteMusicProBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 𝐀𝐬𝐢𝐬𝐭𝐚𝐧", url="https://t.me/MajesteMusicProAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/MacroPem"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝐊𝐨𝐦𝐮𝐭𝐥𝐚𝐫" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 Sohbet Grubu", url=f"https://t.me/MajesteSohbetTr"
                    )
                ]
                
           ]
        ),
    )
