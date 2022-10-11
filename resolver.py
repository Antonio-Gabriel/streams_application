import io
import json

from time import sleep
from threading import Thread

def resolve_bulk_json_data(data: bytes):
    yield data

bulk_data = {
    "users": []
}

def process_data_to_thread(row: str | bytes, index):
    bulk_data["users"].append(row)
    print(f"Row[{index}]> Pushed to transactions list with successffully")   
    
    sleep(2)             

def trait_data_response(row: bytes):
    response = row.replace('\n', '')
    response = response.replace('}{', '},{')
    response = "[" + response + "]"
    return response

def download_file():
    print("File downloaded")
    pass

threads = []
with io.open("bulkData.file", "r") as file:
    # Here we can see that the data is being processed in small bytes
    data = file.read(20*(1024**2))
    for row in resolve_bulk_json_data(data):            
        response = trait_data_response(row)
        json_response = json.loads(response)

        for index, trans_data in enumerate(json_response):                    
            thread = Thread(target=process_data_to_thread, args=(trans_data,index,))
            threads.append(thread)        

for thread in threads:
    thread.start()    

for thread in threads:
    thread.join()

    if thread.is_alive() is False:
        with open("data/transactions.json", "w+") as file:
            file.write(json.dumps(bulk_data, indent=1))     

        download_file()
        print("Process finished")

        break
