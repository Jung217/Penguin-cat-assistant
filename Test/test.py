elif re.match('後製示範',message):
        video_message = VideoSendMessage(
            original_content_url='https://imgur.com/TxrFM93',
            preview_image_url='https://imgur.com/9lDJ8nH'
        )
line_bot_api.reply_message(event.reply_token, video_message)