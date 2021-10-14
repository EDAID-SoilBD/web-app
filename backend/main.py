from flask import Flask, request, Response
from flask_pymongo import pymongo
from bson import json_util

conn = pymongo.MongoClient(
    "mongodb+srv://olegbrz:ZbPObMewgvMS1iqu@edaid-soil.hflhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
database = conn.get_database("SoilDB")
db_col = pymongo.collection.Collection(database, "Data")

app = Flask(__name__)


@app.route("/data", methods=["GET"])
def list_soil_data():
    soil_data = list(db_col.find())
    response = json_util.dumps(soil_data, ensure_ascii=False).encode("utf8")
    return Response(response)


@app.route("/data/<code>", methods=["GET"])
def get_soil_data_entry(code):
    user = db_col.find_one({"CODE": code})
    response = json_util.dumps(user, ensure_ascii=False).encode("utf8")
    return Response(response)


@app.route("/data", methods=["POST"])
def insert_soil_data():
    try:
        item = {
            "CÓDIGO": request.json["CÓDIGO"],
            "FOTOGRAFÍAS": request.json["FOTOGRAFÍAS"],
            "DESCRIPCIÓN": request.json["DESCRIPCIÓN"],
            "COORDENADAS X": request.json["COORDENADAS X"],
            "COORDENADAS Y": request.json["COORDENADAS Y"],
            "ALTITUD": request.json["ALTITUD"],
            "PENDIENTE": request.json["PENDIENTE"],
            "GRAVAS": request.json["GRAVAS"],
            "ARENAS MUY GRUESAS": request.json["ARENAS MUY GRUESAS"],
            "ARENAS GRUESAS": request.json["ARENAS GRUESAS"],
            "ARENAS MEDIAS": request.json["ARENAS MEDIAS"],
            "ARENAS FINAS": request.json["ARENAS FINAS"],
            "ARENAS MUY FINAS": request.json["ARENAS MUY FINAS"],
            "ARENAS TOTALES": request.json["ARENAS TOTALES"],
            "LIMOS GRUESOS": request.json["LIMOS GRUESOS"],
            "LIMOS FINOS": request.json["LIMOS FINOS"],
            "LIMOS TOTALES": request.json["LIMOS TOTALES"],
            "ARCILLAS": request.json["ARCILLAS"],
            "FACTOR K": request.json["FACTOR K"],
            "DENSIDAD APARENTE": request.json["DENSIDAD APARENTE"],
            "ESTABILIDAD DE AGREGADOS": request.json["ESTABILIDAD DE AGREGADOS"],
            "PERMEABILIDAD": request.json["PERMEABILIDAD"],
            "CAPACIDAD DE CAMPO": request.json["CAPACIDAD DE CAMPO"],
            "PUNTO DE MARCHITEZ PERMANENTE": request.json[
                "PUNTO DE MARCHITEZ PERMANENTE"
            ],
            "HIDROFOBICIDAD": request.json["HIDROFOBICIDAD"],
            "CARBONO ORGÁNICO": request.json["CARBONO ORGÁNICO"],
            "FACTOR C": request.json["FACTOR C"],
            "CONDUCTIVIDAD ELÉCTRICA": request.json["CONDUCTIVIDAD ELÉCTRICA"],
            "RESPUESTA ESPECTRAL": request.json["RESPUESTA ESPECTRAL"],
        }

        db_col.insert_one(item)
        status_code = Response(status=201)
    except Exception:
        status_code = Response(status=404)

    return status_code


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
