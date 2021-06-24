from time import sleep

from youtubechat import YoutubeLiveChat, get_live_chat_id_for_stream_now, LiveChatApi, get_live_chat_id_for_broadcast_id, get_livechat_id
import sys

args = sys.argv

#livechat_id = get_live_chat_id_for_broadcast_id('bHySf8pHg_g', "oauth_creds")
livechat_id = get_livechat_id('AIzaSyCF2euzeqte9JeERSG9j80SJqCGKailPX8', args[1])
print(livechat_id)
chat_obj = YoutubeLiveChat("oauth_creds", [livechat_id])
#chat_obj = LiveChatApi(['https://www.youtube.com/watch?v=gfiPOgsNO2M'])


def send(msg, chatid):
    for m in msg:
        print(m)
        print(type(m))
        m.delete()
        chat_obj.send_message(":/ :P", chatid)

#chat_obj.live_chat_messages_insert('Hello to everyone')

chat_obj.start()
chat_obj.send_message(args[2], livechat_id)
#chat_obj.send_message('Hi zztop 2.', livechat_id)
chat_obj.subscribe_chat_message(send)
chat_obj.join()
chat_obj.stop()