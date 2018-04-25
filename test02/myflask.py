# _*_encoding:utf-8_*_
from flask import Flask,request,render_template,json

app = Flask(__name__)

#验证key和key_src的值是和数据中的匹配，并返回对应的值
def Verification(data):
    key = '111'
    key_src = '12345'
    if data.get("key") == key and data.get("key_src") == key_src:
        return json.dumps(data["data"])
    else:
        return "你的key和key_src值不对，请检查！"


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.get_data()
        data_s = json.loads(data)
        s = Verification(data_s)
        print(s)
        return s
    else:
        return render_template('404.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=88)
