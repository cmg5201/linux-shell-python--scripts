import commodity

#显示商品信息
def show_commodity_detail(commodity):
    print("========== 商品信息 ==========")
    commodity_id = commodity.get("commodity_id","暂无")    #get():如果有commodity_id，就返回它；如果没有，就返回暂无,用来兼容旧数据
    print(f"商品编号: {commodity_id}")
    print(f"商品名称:{commodity['commodity_name']}")
    print(f"商品价格:{commodity['commodity_price']}")
    print(f"商品数量:{commodity['commodity_quantity']}")
    print(f"总价格:{commodity['total_price']}")
    print("==============================")


#添加商品
def add_commodity(commodity_list):

    try:
        commodity_name=input("请输入添加的商品名称:")
        if commodity_name=="":
            raise ValueError("添加的商品名称不能为空")  #raise:制造一次异常错误让try监测到

        for item in commodity_list:
            if commodity_name==item["commodity_name"]:
                raise ValueError("该商品已存在,不能重复添加")

        commodity_price=float(input("请输入商品价格:"))
        if commodity_price<=0:
            raise ValueError("商品价格必须大于0")

        commodity_quantity=int(input("请输入商品数量:"))
        if commodity_quantity<=0:
            raise ValueError("商品数量必须大于0")

        commodity_id=create_commodity_id(commodity_list)


        new_commodity={
            "commodity_id":commodity_id,
            "commodity_name":commodity_name,
            "commodity_price":commodity_price,
            "commodity_quantity":commodity_quantity
        }
        new_commodity["total_price"]=new_commodity["commodity_price"]*new_commodity["commodity_quantity"]

       #把商品添加到列表
        commodity_list.append(new_commodity)

        #保存到json文件
        commodity.save_commodity_data(commodity_list)

        return new_commodity
    except ValueError as e:
        print(e)
        return False




#查询商品
def find_commodity(commodity_list):

    try:

        keyword=input("请输入查询关键词:")
        if keyword=="":
            raise ValueError("关键词不能为空!")

        result_list=[]

        for item in commodity_list:
            if keyword.lower() in item["commodity_name"].lower():
                result_list.append(item)

        return result_list

    except ValueError as e:
        print(e)
        return False

        return []





#查询所有商品
def show_all_commodity(commodity_list):
    print("========== 商品列表 ==========")
    for item in commodity_list:
        show_commodity_detail(item)
        print()
    print("==============================")



#修改商品
def update_commodity(commodity_list):

    try:

        update_commodity_id=int(input("请输入需要修改的商品编号:"))


        for item in commodity_list:
            if item.get("commodity_id")==update_commodity_id:

                show_commodity_detail(item)

                confirm=input("是否修改该商品?(y/n):")

                if confirm.lower() !="y":   #lower():将字符串全部小写
                    print("取消修改")
                    return False

                new_price= float(input("请输入需要修改的价格:"))
                if new_price<=0:
                    raise ValueError("商品价格必须大于0")

                new_quantity=int(input("请输入需要修改的数量:"))
                if new_quantity<=0:
                    raise ValueError("商品数量必须大于0")


                item["commodity_price"] = new_price
                item["commodity_quantity"]=new_quantity
                item["total_price"]=item["commodity_price"]*item["commodity_quantity"]

                commodity.save_commodity_data(commodity_list)

                return True

        print("没有找到该商品")
        return False

    except ValueError:
        print("商品编号必须是数字")
        return False





#删除商品
def delete_commodity(commodity_list):
    try:

        delete_id=int(input("请输入需要删除的商品编号:"))

        commodity_to_delete = None

        for item in commodity_list:

            if item.get("commodity_id")==delete_id:

                commodity_to_delete = item

                show_commodity_detail(commodity_to_delete)

                break

        if commodity_to_delete:

            confirm=input("确认删除该商品吗?(y/n):")

            if confirm.lower() !="y":
                print("取消删除")
                return False

            commodity_list.remove(commodity_to_delete)

            commodity.save_commodity_data(commodity_list)
            return True


        print("没有找到商品")
        return False

    except ValueError:
        print("商品编号必须是数字")
        return False


#添加商品id
def create_commodity_id(commodity_list):
    if len(commodity_list)==0:
        return 1001

    max_id=1000

    for item in commodity_list:
        commodity_id=item.get("commodity_id")

        if commodity_id is not None:
            if item["commodity_id"]>max_id:
                max_id=item["commodity_id"]

    return max_id + 1


def update_commodity_id(commodity_list):    #给没有商品编号的商品自动补编号

    next_id=create_commodity_id(commodity_list)

    updated= False

    for item in commodity_list:
        if item.get("commodity_id") is None:
            item["commodity_id"] = next_id
            next_id += 1   #编号自动增加
            updated = True
    return updated



#编号查询
def find_commodity_by_id(commodity_list):
    try:
        commodity_id=int(input("请输入商品编号:"))

        for item in commodity_list:
            if item.get("commodity_id")==commodity_id:
                return item
        return False
    except ValueError :
        print("商品编号必须是数字")
        return False
