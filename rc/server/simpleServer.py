from flask import Flask
app=Flask(import_name=__name__,static_url_path="",static_folder="../../rc/static/")
@app.route(rule="/")
def fIndex():
    return "Flask App"
if __name__=="__main__":
    app.run(debug=True)
    
cars=[
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]
