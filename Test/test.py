    elif re.match("金門大學在哪",message):
        location_message = LocationSendMessage(
            title= "國立金門大學", 
            address= "892金門縣金寧鄉大學路1號",
            latitude= 24.44829638687612,  
            longitude= 118.32249208222159
            )
l       line_bot_api.reply_message(event.reply_token, location_message)