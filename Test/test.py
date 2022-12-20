    elif re.match("恭喜",message):
        sticker_message = StickerSendMessage(
            package_id='6325',
            sticker_id='10979924'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)