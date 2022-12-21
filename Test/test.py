if "股票 " in message:
         buttons_template_message = TemplateSendMessage(
         alt_text = "股票資訊",
        template=CarouselTemplate( 
            columns=[ 
                    CarouselColumn( 
                        thumbnail_image_url ="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                        title = message + " 股票資訊", 
                        text ="請點選想查詢的股票資訊", 
                        actions =[
                            MessageAction( 
                                label= message[3:] + " 個股資訊",
                                text= "個股資訊 " + message[3:]),
                            MessageAction( 
                                label= message[3:] + " 個股新聞",
                                text= "個股新聞 " + message[3:])
                        ]
                    )
                ]
            )
         )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)