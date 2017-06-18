from flask import Flask
import Capio
import json
import pprint

app = Flask(__name__)

@app.route("/")
def capio():
    with open('config.json') as json_data_file:
        config_data = json.load(json_data_file)
    status,response = Capio.fetch_from_api(config_data['url'], config_data['transcript_id'],
                                           config_data['api_key'])
    if status!="error":
        try:
            Capio.parse_json(response, config_data['file_path'])
            final_status = "The API call was successful. The reponse has been parsed and stored in the file"
        except Exception as e:
            final_status = "The API call was successful. But there was some error parsing the file" + str(e)
        return final_status
    else:
        return "There was some problem with the API call"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
