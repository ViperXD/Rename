import pyrogram

from plugins.Zee5_dl import zee5_execute


@pyrogram.Client.on_callback_query()
async def formatbuttons(bot, update):
       
    if "|" in update.data:
        await zee5_execute(bot, update)

    elif query.data == "start_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤔Help", callback_data="help_data"),
                    InlineKeyboardButton("🤖About", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "Close🔒", callback_data="closeformat")
                ]
            ]
        )

        await query.message.edit_text(
            translation.START_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "help_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🏠Home', callback_data='start_data'),
                    InlineKeyboardButton('About🤖', callback_data='about_data'')
                ]
            ]
        )

        await query.message.edit_text(
            translation.HELP_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    elif query.data == "about_data":
        await query.answer()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🏃🏻‍♂️Back', callback_data='start_data'),
                    InlineKeyboardButton('Help🤔', callback_data='help_data')
                ]
            ]
        ),

        await query.message.edit_text(
            translation.ABOUT_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return
        
    elif "closeformat" in update.data:     
        await update.message.delete() 
