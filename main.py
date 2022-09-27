from flask import Flask , render_template ,request
import pandas as pd
import os
import model as m
app = Flask(__name__)

DATASETS_PATH = "C:/Users/Amir/technolab"
df_recommend = pd.read_csv(os.path.join(DATASETS_PATH, 'cluster_recommend_dataset.csv'))


@app.route("/")
def hello():
    return render_template("index.html" )
@app.route("/sub",methods = ['POST'])
def result():
    if request.method == "POST":
        songname = request.form['songname']
        number = request.form['quantity']
        songs = m.recommend_me_by_track(songname, number)
        s = songs
    return render_template("sub.html", result=[s.to_html(classes='data')], titles=s.columns.values,n=number)
if __name__ == "__main__":
    app.run(debug=True)
