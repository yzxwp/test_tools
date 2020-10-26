import ID_Card.get_address as em
import ID_Card.get_idcard as id
import ID_Card.get_name as na
import ID_Card.get_tellphone as ph
import ID_Card.get_creditID as cre

def get_message():
    email = em.RandomEmail()
    card = id.ident_generator()
    name = na.random_name()
    phone = ph.phone_num()
    credit=cre.create_social_credit()
    return email + '  ' + card + '  ' + name + '  ' + phone+'  '+credit

def get_count():
    count = input("请输入一个整数(获取多少条数据)：")
    #判断输入值是不是整数
    try:
        count=int(count)
        # junage=isinstance(count , int)
        return count
    except:
        print('您输入的不是整数,请重新输入:')
        return get_count()

def writte(count):
    data=u'   用户邮箱 ---- 身份证号码 ---- 用户姓名 ---- 电话 ---- 统一社会征信码                                  '
    print(data)
    with open(r'./output/message.txt', 'w') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(data)  # 写入
        file_handle.write('\n')
    for i in range(0,count):
        with open(r'./output/message.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
            data1=get_message()
            file_handle.write(data1)  # 写入
            print(data1)
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据




