from flask import Flask
app=Flask(__name__,static_url_path="",static_folder="../../rc/static/")
@app.route("/")
def fIndex():
    return "Flask App"
if __name__=="__main__":
    app.run(debug=True)
    