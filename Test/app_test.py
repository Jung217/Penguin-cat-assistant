from imgurpython import ImgurClient
from datetime import datetime


def upload(client_data, local_img_file, album , name = 'test-name!' ,title = 'test-title' ):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }

    print("Uploading image... ")
    image = client_data.upload_from_path(local_img_file, config=config, anon=False)
    print("Done")

    return image


if __name__ == "__main__":
    client_id ='d8f43d95eef9f03'
    client_secret = 'feb68e5f92b414abe07b733f052a28d178014f32'
    access_token = "9186d34380cec7f4896f65addc9ca95f6022ba39"
    refresh_token = "52394ee41eec3876be8484cbb5ede2e63ebf2d1d"
    album = "a/DTCcvw"
    local_img_file = "test.png"
    
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    image = upload(client, local_img_file, album)
    print(f"圖片網址: {image['link']}")