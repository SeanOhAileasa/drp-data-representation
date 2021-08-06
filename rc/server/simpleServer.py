from flask import Flask
app=Flask(import_name=__name__,static_url_path="",static_folder="../../rc/static/")
# repository ./drp-data-representation
@app.route(rule="/",methods=["GET"])
def fIndex():
    """URL map for "/".

Input: 
Process: 
Output: string
"""    
    return "Flask App"
# --- END ---
# repository ./drp-data-representation
@app.route(rule="/get-all-cars/")
def fGetAllCars():
    """URL map for "/get-all-cars/".

Input: 
Process: (flask.json.jsonify)
Output: all cars
"""
    from flask.json import jsonify
    return jsonify({"allCars":cars})
# --- END ---
# repository ./drp-data-representation
@app.route(rule="/get-all-cars/<string:nParReg>")
def fGetCar(nParReg):
    """URL map for anything after "/get-all-cars/".

Input: nParReg
Process: (lambda; filter; list; flask.json.jsonify)
Output: first car registration match
"""
    from flask.json import jsonify
    nFoundCars=list(filter(lambda n:n["reg"]==nParReg,cars))
    if len(nFoundCars)==0:
        return jsonify({"theCar":""}),204
    return jsonify({"theCar":nFoundCars[0]}) 
# --- END ---
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
if __name__=="__main__":
    app.run(debug=True)
