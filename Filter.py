import os
import json
from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb+srv://<USERNAME?:<PASSWORD>@<DATABASE URL>/test?retryWrites=true&w=majority")


connection = Connect.get_connection()
db = connection.MapUTM
serverStatusResult = db.command("serverStatus")
directory = './all_courses'
building_code = "DH"

for filename in os.listdir(directory):
    found = False
    if filename.endswith(".json"):
        with open(directory + "/" + filename) as json_file:
            file_contents = json.load(json_file)
            room = {
                "classes": []
            }
            for section in file_contents["meeting_sections"]:
                for time in section["times"]:
                    if building_code in time["location"]:
                        course = {
                            "course_code": file_contents["code"][0:9],
                            "name": file_contents["name"],
                            "lec_code": section["code"],
                            "times": {"day": time["day"],
                                      "start": time["start"] / 3600,
                                      "end": time["end"] / 3600,
                                      "duration": time["duration"] / 3600}
                        }
                        if db.Deerfield.find_one({"room": time["location"]}) is None:
                            room["room"] = time["location"]
                            room["classes"].append(course)
                            db.Deerfield.insert_one(room)
                        else:
                            db.Deerfield.find_one_and_update({"room": time["location"]},
                                                             {"$addToSet": {"classes": course}})
