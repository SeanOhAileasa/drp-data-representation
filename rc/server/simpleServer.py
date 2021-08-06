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
# repository ./drp-data-representation
@app.route(rule="/get-all-cars",methods=["POST"])
def fCreateCar():
    """Create new car.

Input:
Process: (flask.request; flask.abort; append; flask.json.jsonify)
Output: return new car with status code 201 
"""
    from flask import request,abort,jsonify
    if not request.json:
        abort(400)
    if not "reg" in request.json:
        abort(400)
    nObjNewCar={
        "reg":request.json["reg"],
        "make":request.json["make"],
        "model":request.json["model"],
        "price":request.json["price"]
    }
    cars.append(nObjNewCar)
    return jsonify({"car":nObjNewCar}),201
# --- END ---
# repository ./drp-data-representation
@app.route("/get-all-cars/<string:nParReg>",methods=["PUT"])
def fUpdateCar(nParReg):
    """Update existing car.

Input: nParReg
Process: (lambda; filter; list; len; flask.abort; flask.request; type; flask.json.jsonify)
Output:
"""    
    from flask import request,abort,jsonify
    nFoundCars=list(filter(lambda t:t["reg"]==nParReg,cars))
    if len(nFoundCars)==0:
        abort(404)
    if not request.json:
        abort(400)
    if "make" in request.json and type(request.json["make"])!=str:
        abort(400)
    if "model" in request.json and type(request.json["model"]) is not str:
        abort(400)
    if "price" in request.json and type(request.json["price"]) is not int:
        abort(400)
    nFoundCars[0]["make"]=request.json.get("make",nFoundCars[0]["make"])
    nFoundCars[0]["model"]=request.json.get("model",nFoundCars[0]["model"])
    nFoundCars[0]["price"]=request.json.get("price",nFoundCars[0]["price"])
    return jsonify({"car":nFoundCars[0]})
# --- END ---
# repository ./drp-data-representation
@app.route("/get-all-cars/<string:nParReg>",methods=["DELETE"])
def fDeleteCar(nParReg):
    """Delete a car.

Input: nParReg
Process: (lambda; filter; list; len; flask.abort; remove; flask.json.jsonify)
Output:
"""
    from flask import abort,jsonify
    nFoundCars=list(filter(lambda z:z["reg"]==nParReg,cars))
    if len(nFoundCars)==0:
        abort(404)
    cars.remove(nFoundCars[0])
    return jsonify({"result":True})
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
