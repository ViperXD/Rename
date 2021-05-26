import pyrogram

from plugins.Zee5_dl import zee5_execute


@pyrogram.Client.on_callback_query()
async def formatbuttons(bot, update):
       
    if "|" in update.data:
        await zee5_execute(bot, update)

    elif query.data == "help_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("", url="https://youtu.be/hkmc3e7U7R4"),
                    InlineKeyboardButton("About Me", callback_data="about_data")
                ],
                [
                    InlineKeyboardButton("BOT Channel", url="https://t.me/TroJanzHEX"),
                    InlineKeyboardButton("Support Group", url="https://t.me/TroJanzSupport")
                ]
            ]
        )

        await query.message.edit_text(
            Script.HELP_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE", url="https://github.com/TroJanzHEX/Unlimited-Filter-Bot")
                ],
                [
                    InlineKeyboardButton("BACK", callback_data="help_data"),
                    InlineKeyboardButton("CLOSE", callback_data="close_data"),
                ]                
            ]
        )

        await query.message.edit_text(
            Script.ABOUT_MSG,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return
        
    elif "closeformat" in update.data:     
        await update.message.delete() 
