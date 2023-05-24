import json
import requests
import ast
import os


def translator(str):
    """
    input : str 需要翻译的字符串
    output：translation 翻译后的字符串
    """
    # API
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数， i为要翻译的内容
    key = {
        'type': "AUTO",
        'i': str,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        result = json.loads(response.text)
        translation = result['translateResult'][0][0]['tgt']
        return translation
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None


txtFilepath = "targets"
saveFilepath = "results"
total_txt = os.listdir(txtFilepath)
num = len(total_txt)
lists = range(num)  # 创建从0到num的整数列表
files = os.listdir(saveFilepath)
for i in lists:
    with open("targets/" + total_txt[i], 'r', encoding='utf8') as fp:
        jsonStr = json.load(fp)
    needTrans = ["description", "name"]
    for key in needTrans:
        if not jsonStr.get(key): continue
        jsonStr[key] = translator(jsonStr[key])

    with open("results/" + total_txt[i], "w", encoding='utf-8') as f:
        json.dump(jsonStr, f, indent=2, sort_keys=True, ensure_ascii=False)
