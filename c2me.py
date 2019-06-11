from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route("/")
def index():
    url = "https://api.c2me.cc/b/shuffle_filter?password=atacan&gender=f&age_start=18&nick=atacan&order_by_last_online=1&age_stop=40"
    response = requests.get(url)
    json_verisi=response.json()
    online_people=json_verisi["online_users"]
    sozluk=[]

    for person in online_people:
        sozluk.append(person["nick"])
        
    return render_template("index.html",data = sozluk)
if  __name__ == "__main__":
    app.run(debug=True)