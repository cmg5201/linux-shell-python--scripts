import os
import json


# 保存商品列表到json
def save_commodity_data(commodity_list):

    with open("commodity_data.json","w",encoding="utf-8") as file:
        json.dump(commodity_list,file,ensure_ascii=False,indent=4)



# 读取json文件
def load_commodity_data():
    if not os.path.exists("commodity_data.json"):    #os.path.exists() :判断文件是否存在
        with open("commodity_data.json","w",encoding="utf-8") as file:
            json.dump([],file,ensure_ascii=False,indent=4)

    with open('commodity_data.json', 'r', encoding='utf-8') as file:
        commodity_list = json.load(file)
    return commodity_list
