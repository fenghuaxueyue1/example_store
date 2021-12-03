import time
import hashlib

import requests


class __AvatarStyleConst:

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value


# MP 人物轮廓(不因电子邮件哈希而异)
MP = __AvatarStyleConst("mp")
# GEOMETRIC 几何
GEOMETRIC = __AvatarStyleConst("identicon")
# MONSTER 怪物
MONSTER = __AvatarStyleConst("monsterid")
# FACE 人脸
FACE = __AvatarStyleConst("wavatar")
# RETRO 复古像素
RETRO = __AvatarStyleConst("retro")
# ROBOT 机器人
ROBOT = __AvatarStyleConst("robohash")


# Generate Random Portrait
class Avatar:

    def __init__(self, style: str, size: int):
        self.style = style
        self.size = size

    def generate(self, origin: str):
        if not origin:
            origin = str(time.time_ns())

        origin = origin.lower().lstrip().rsplit()
        hash_str = hashlib.md5("{}".format(origin).encode("utf-8")).hexdigest()
        url = 'https://cn.gravatar.com/avatar/{}?d={}&s={}'.format(hash_str, self.style, self.size)
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return url

        return None