import json
import requests
import ast


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


with open('en_us.json', 'r', encoding='utf8') as fp:
    jsonStr = ""
    for line in fp.readlines():
        if "//" not in line:
            jsonStr += line

needTran = ast.literal_eval(jsonStr)
for key, value in needTran.items():
    needTran[key]=translator(value)

with open("zh_cn.json", "w", encoding='utf-8') as f:
    json.dump(needTran, f, indent=2, sort_keys=True, ensure_ascii=False)