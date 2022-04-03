from flask import Flask,jsonify,request

 

app=Flask(__name__)


contacts=[
    {
        "id":1,
        "title":"study",
        "description":"study of maths",
        "done":False

    },
    {
        "id":2,
        "title":"studyscience",
        "description":"study of science",
        "done":False

    }
]
@app.route("/")
def helloworld():
    return "hello world"


@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    
    contact={
        "id":contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    contacts.append(contact)

    return jsonify({

        "status":"success",
        "message":"contact added successfully"
    })

@app.route("/get-data")
def getcontact():
    return jsonify({
        "data":contacts
    })

if(__name__=="__main__"):
    app.run(debug=True)
 