from chatpy.api import API
from chatpy.auth import TokenAuthHandler
from environs import Env

env = Env()
env.read_env()


def handler(data):
    auth = TokenAuthHandler(env('CHATWORK_TOKEN'))
    api = API(auth, api_root='/v2')
    data = filter(lambda x: x.get('status') != 'Resolved', data)
    if data:
        members = "\n".join([item.get('assigned_to') for item in data])

        body = "[toall]" \
               "[info][title]Danh sach members chưa hoàn thành Monthly report[/title][code]{0}[/code]Hiện tại em không thấy thông tin các bài monthly report của các anh chị trên redmine tháng này.\n" \
               "Các anh chị vui lòng hoàn thành sớm trước ngày 20 hàng tháng để Team Lead và Group leader thực hiện review" \
               "\n\n" \
               "Thank you!!![/info]".format(members)

        api.post_message(**{'room_id': '176758731', 'body': body})
