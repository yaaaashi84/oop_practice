"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算
"""


# classとは、雛形のようなものでそこに各個人の情報を代入していく


class BMI:
    """docstring for BMI."""

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = self.weight / (self.height**2)
        if float(10.0) <= self.bmi <= float(40):
            return None  # initの中で、returnの結果を返してしまうと、開始の処理を邪魔してしまう。initの中でreturnの後はpassかNoneにすること。
        elif int(10) > self.bmi:
            raise ValueError("too skinny")
        else:
            raise ValueError("too fat")

    def __str__(self):
        return f"{self.bmi:.2f}"


# tanaka = BMI(height=1.80, weight=67.0)
# sasami = BMI(height=1.58, weight=80.0)

name_height = float(input("あなたの身長は？ > "))
name_weight = float(input("あなたの体重は？ > "))

name = BMI(height=name_height, weight=name_weight)
print(name)

# def
# if 10 <= self.bmi <= 40:
#     return print(self.bmi)
# if self.bmi < 10:
#     return print("too skiny")
# if self.bmi > 40:
#     return print("too fat")

# def calculate_bmi(self): # ()のなかにselfを入れることでこの関数内でself関連の変数を使うことができる
#     # BMI = 体重÷身長の2剰
#     return self.weight / (self.height ** 2)

# インスタンス


# tanaka_bmi = BMI(height=1.80, weight=67.0)
# sasami_bmi = BMI(height=1.58, weight=80.0)

# # tanaka_bmiの身長を出力
# print(tanaka_bmi.height)  # classの中の設定した値がプロパティ(計算など関数を使っていないもの)

# # BMIの出力
# print(tanaka_bmi.bmi)  # ()の中に関数呼び出したときにつけておく

# tanaka_bmi.bmiのようにドットで繋ぐときは両方の計算式や関数を用いるということ。そして、そこにselfは除いた値で記入する。

# if 10 <= int(tanaka_bmi.bmi) <= 40:
#     print(tanaka_bmi)
# else:
#     print("error")
# def __str__()の関数を定義することで、この一行でreturnによってBMIを返すことができる。
