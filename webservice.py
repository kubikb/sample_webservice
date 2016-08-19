from flask import Flask, jsonify, request
import logging
import json
import random

# Setup logging
logging.basicConfig(format='[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)s - %(message)s',
                    level=logging.DEBUG)
flask_logger = logging.getLogger("werkzeug")
flask_logger.setLevel(logging.DEBUG)

# Flask object
application = Flask(__name__)

# List of sample movies
movies_list = ["Snakes on the Plane",
               "Vertigo",
               "Drama alert",
               "Django",
               "SZISZ"]

@application.route("/", methods=['GET', 'POST'])
def manage_calls():
    if request.method == "GET":
        return jsonify({"Tableau Recommendation Engine WebService": "OK"}), 200

    elif request.method == "POST":
        logging.info("Tableau Recommendation Engine WebService received the following JSON:")
        message = request.get_json()
        logging.info(json.dumps(message, indent=4, sort_keys=True))

        # Only process JSON if it contains the key 'user_id'
        if message.keys() == ["user_id"]:
            user_id = message.get("user_id")

            logging.debug("Received JSON looks valid. Getting movie recommendations for user %s" %user_id)

            # Get a sample from movies_list
            sample_movies = random.sample(movies_list, 3)

            # Return the sample to the requestor
            results = sample_movies
            logging.info("Returning the following result:")
            logging.info(json.dumps(results, indent=4, sort_keys=True))
            return jsonify({"Result for user %s" %user_id : results}), 200
        else:
            logging.error("Received JSON is not valid!")
            return jsonify({"ERROR": "JSON did not contain the key 'user_id'!"}), 500

if __name__ == "__main__":
    application.run(host='0.0.0.0',
                    port=5000)