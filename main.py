import commodity
import commodity_manage

def main():

    commodity_list=commodity.load_commodity_data()
    updated=commodity_manage.update_commodity_id(commodity_list)
    if updated:
        commodity.save_commodity_data(commodity_list)


    while True:
        print("=====商品管理系统=====")
        print("1.添加商品")
        print("2.关键字查询")  #模糊搜索
        print("3.编号查询")   #精确搜索
        print("4.查看全部商品")
        print("5.修改商品")
        print("6.删除商品")
        print("7.退出系统")

        choice=input("请选择功能:")

        if choice=="1":
            result=commodity_manage.add_commodity(commodity_list)
            if result:
                print("商品新增成功")
                print(result)
            else:
                print("商品新增失败")

        elif choice == "2":
            result=commodity_manage.find_commodity(commodity_list)
            if result:
                print("查询结果:")

                for item in result:
                    commodity_manage.show_commodity_detail(item)

            else:
                print("没有找到该商品")

        elif choice == "3":
            result=commodity_manage.find_commodity_by_id(commodity_list)
            if result:
                print("查询成功")
                commodity_manage.show_commodity_detail(result)
            else:
                print("没找到该商品")

        elif choice == "4":
            commodity_manage.show_all_commodity(commodity_list)

        elif choice == "5":
            result=commodity_manage.update_commodity(commodity_list)
            if result:
                print("商品信息修改成功")
            else:
                print("商品信息修改失败")

        elif choice == "6":
            result=commodity_manage.delete_commodity(commodity_list)
            if result:
                print("商品信息删除成功")
            else:
                print("商品信息删除失败")

        elif choice == "7":
            print("程序退出")
            break

        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()

