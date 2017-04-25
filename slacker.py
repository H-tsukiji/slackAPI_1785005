# -*- coding: utf-8 -*-
from slacker import Slacker
 
class Slack(object):
 
    __slacker = None
 
    def __init__(self, token):
 
        self.__slacker = Slacker(token)
 
    def get_channnel_list(self):
        """
        Slackチーム内のチャンネルID、チャンネル名一覧を取得する。
        """
 
        # bodyで取得することで、[{チャンネル1},{チャンネル2},...,]の形式で取得できる。
        raw_data = self.__slacker.channels.list().body
 
        result = []
        for data in raw_data["channels"]:
            result.append(dict(channel_id=data["id"], channel_name=data["name"]))  
 
        return result
 
if __name__ == "__main__":
 
    slack = Slack("xoxp-18292672947-18354986291-166689903238-d1ff9554866a15e73129eb85d808d055")
 
    print(slack.get_channnel_list())