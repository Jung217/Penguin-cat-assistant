from imgurpython import ImgurClient

client_id = 'd8f43d95eef9f03'
client_secret = '01067fd51b3a4f19591fd6fd7f06652e803e30c2'
album_id = 'a/u8HqBZL'
access_token = '9186d34380cec7f4896f65addc9ca95f6022ba39'
refresh_token = '52394ee41eec3876be8484cbb5ede2e63ebf2d1d'

if __name__ == "__main__":
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    config = {
        'album': album_id,
        'name': 'Test',
        'title': 'Test',
        'description': 'Test'
    }
    print("Uploading image... ")
    image = client.upload_from_path('test.png', config=config, anon=False)
    print("Done")