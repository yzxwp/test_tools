# encoding:utf8
import random
import re


def chepaihao(len=6):
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，可自行百度
    char2 = '1234567890ABCDEFGHJKLMNPQRSTUVWXYZ'
    char3 = '1234567890'
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    len3 = len(char3) - 1
    while True:
        code = ''
        index0 = random.randint(1, len0)
        index1 = random.randint(1, len1)
        code += char0[index0]
        code += char1[index1]
        code += ' '
        for i in range(1, 5):
            index2 = random.randint(1, len2)
            code += char2[index2]
        index3 = random.randint(1, len3)
        code += char3[index3]
        test = re.match('^.\w.[A-Z]\d{4}$|^.\w.\d[A-Z]\d{3}$|^.\w.\d{2}[A-Z]\d{2}$|^.\w.\d{3}[A-Z]\d$|^.\w.\d{5}$',
                        code)
        if test:
            return code


if __name__ == '__main__':
    print(chepaihao(len))
