# Capio
File description:
1.) Config.json
This is the configuration file for this Application containing URL, API key, Output File Path and Transcription ID. 

2.)Capio.py
This python file fetches the response for the given URL, Transcript_id and API_key. The fetched JSON response is parsed and written to the document in the given format. The path where the output doc gets stored can be modified in the Config.json file.

3.) CapioTest.py
This is the Unit Test file created using Unittest module. 

4.)app.py
This is the Flask application file.

5.)requirements.txt
This contains the list of dependencies required to run this app. This file will be utilised by Docker.

6.)Dockerfile
This is the Specification file for creating a Docker container for this application.

Steps to run:
1.) Using Docker:
The above files are put in a directory and the following commands are run in that directory.
--> docker build -t <Image_name>:latest .
--> docker run -d -p 5000:5000 <Image_name>
--> Test the container by going to the address - "http://0.0.0.0/5000/" in your browser. If API response is succesful, the doc can be opened and checked in the location mentioned in config.json.
The web server will output success message if the transcription is written successfully or it will output error message.
To see the created file in container:
The following command is used on a running container- "docker exec -it <container_name> bash" and the filesystem can be browsed and the output file can be viewed/copied to host.

2.) Without Docker
-->python app.py
--> Go to the address - "http://0.0.0.0/5000/" in your browser for the API response and if succesful, the doc can be opened and checked in the location mentioned in config.json.

3.) For running test cases:
python CapioTest.py
