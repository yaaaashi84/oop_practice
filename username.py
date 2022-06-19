"""
データ型:UserName
    属性:
        実際のユーザー名
    ルール:
        ユーザー名は4文字以上20文字以内である
    できること:
        ユーザー名を太文字に変換する
"""


class UserName:
    def __init__(self, name):
        # 4文字以上20文字以内のチェック
        if not(4 <= len(name) and len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")
        self.name = name

    def screen_name(self):
        return self.name.upper()


tanaka = UserName(name='tanaka')  # インスタンス化
# bob = UserName(name='Baba')

print(tanaka.screen_name())
# print(bob.name)