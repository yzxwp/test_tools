import ID_Card.get_address as em
import ID_Card.get_idcard as id
import ID_Card.get_name as na
import ID_Card.get_tellphone as ph
import ID_Card.get_creditID as cre
import ID_Card.get_card as ba
import csv
import pandas as pd
import ID_Card.get_vin as vi
import ID_Card.get_car as ca


# 得到数据
def get_message():
    email = em.RandomEmail()
    card = id.ident_generator()
    name = na.random_name()
    phone = ph.phone_num()
    try:
        credit = cre.create_social_credit()
    except:
        credit = cre.create_social_credit()
    bank_gongshang = ba.gen_bank_card_gonghang()
    bank_nongye = ba.gen_bank_card_nonghang()
    vin = vi.random_vin()
    car = ca.chepaihao(len)
    # return email + '' + card + '' + name + '' + phone + '' + credit + '' + bank_gongshang + '' + bank_nongye
    dic = {"用户邮箱": [email],
           "身份证号码": [card],
           "用户姓名": [name],
           "电话": [phone],
           "统一社会征信码": [credit],
           "工商银行": [bank_gongshang],
           "农业银行": [bank_nongye],
           "车架号": [vin],
           "车牌号": [car]}
    return dic


def get_count():
    count = input("请输入一个大于0小于等于300的整数(获取多少条数据)：")
    # 判断输入值是不是整数
    try:
        count = int(count)
        if  count <= 0 or count>300:
            print("输入值小于等于0或者大于300的，请重新输入：")
            return get_count()
        # junage=isinstance(count , int)
        return count
    except:
        print('不符合要求,请重新输入一个大于0的整数(获取多少条数据):')
        return get_count()


def writte(count):
    data = u'   用户邮箱 ---- 身份证号码 ---- 用户姓名 ---- 电话 ---- 统一社会征信码 --- 工商银行----- 农业银行 --- 车架号 ----车牌号'
    print(data)
    with open(r'../output/message.txt', 'w') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(data)  # 写入
        file_handle.write('\n')
    for i in range(0, count):
        with open(r'../output/message.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
            data1 = get_message()
            file_handle.write(data1)  # 写入
            print(data1)
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据


def wrrite_csv(count):
    header = {"用户邮箱", "身份证号码", "用户姓名", "电话", "统一社会征信码", "工商银行", "农业银行", "车架号", "车牌号"}
    with open(r'../output/message.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()  # 写入列名
    for i in range(0, count):
        with open(r'../output/message.csv', 'a', newline='', encoding='utf-8') as f:
            datas = get_message()
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()  # 写入列名
            writer.writerows(datas)  # 写入数据


def wrrite_csv_by_pandas(count):
    for i in range(0, count):
        data = get_message()
        print(data)
        df = pd.DataFrame(data)
        df.to_csv(r'../output/message.csv', mode='a', encoding='GBK')


def wrrite_csv_by_pandas2(count):
    dic1 = {"用户邮箱": [],
            "身份证号码": [],
            "用户姓名": [],
            "电话": [],
            "统一社会征信码": [],
            "工商银行": [],
            "农业银行": [],
            "车架号": [],
            "车牌号": []}
    for i in range(0, count):
        data = get_message()
        print(data)
        dic1['用户邮箱'] = dic1['用户邮箱'] + data['用户邮箱']
        dic1['身份证号码'] = dic1['身份证号码'] + data['身份证号码']
        dic1['用户姓名'] = dic1['用户姓名'] + data['用户姓名']
        dic1['电话'] = dic1['电话'] + data['电话']
        dic1['统一社会征信码'] = dic1['统一社会征信码'] + data['统一社会征信码']
        dic1['工商银行'] = dic1['工商银行'] + data['工商银行']
        dic1['农业银行'] = dic1['农业银行'] + data['农业银行']
        dic1['车架号'] = dic1['车架号'] + data['车架号']
        dic1['车牌号'] = dic1['车牌号'] + data['车牌号']
    # pd.set_option("display.max_colwidth", 30000)
    df = pd.DataFrame(dic1)
    # pd.set_option('display.expand_frame_repr', False)
    # pd.set_option('display.max_colwidth', 150)
    # print(df)
    # df.to_csv(r'../output/message.csv', encoding='GBK',index=None)
    df.to_csv(r'./output/message.csv', encoding='GBK')


if __name__ == '__main__':
    wrrite_csv_by_pandas2(get_count())
