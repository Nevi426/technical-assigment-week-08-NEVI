import pymongo 
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)

@app.route('/nevi',methods=['POST'])
def sensor():

    dt = datetime.now()
    client = pymongo.MongoClient("mongodb+srv://Nevi:Nevi2006@week-08.nyv6ah6.mongodb.net/?retryWrites=true&w=majority")
    db = client['Week-08']
    my_collections = db['Data']


    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')


    nilai_sensor = {'kecepatan':kecepatan,
                    'latitude':latitude,
                    'longitude':longitude,
                    'timestamp' : dt
                    }

    results = my_collections.insert_one(nilai_sensor)
    return ('data sukses diupload')  
  
  
  
if __name__ == '__main__':
    app.run(debug=True)
