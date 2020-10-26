#encoding=utf-8
import logic.logic_id as lo
def main():
    try:
        while 1:
            lo.writte(lo.get_count())
    except:
        # print("发生未知错误，请重新开始输入")
        main()
if __name__ == '__main__':
    main()
