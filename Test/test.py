WHurl = "https://penguin-cat-assistant.herokuapp.com"
		SendImage = line_bot_api.get_message_content(event.message.id)
		local_save = './static/' + event.message.id + '.png'
		with open(local_save, 'wb') as fd:
			for chenk in SendImage.iter_content():
				fd.write(chenk)
        image_message = ImageSendMessage(
            original_content_url = WHurl + "/static/" + event.message.id + ".png",
            preview_image_url = WHurl + "/static/" + event.message.id + ".png"
        )
		line_bot_api.reply_message(event.reply_token, image_message)