from pymongo import MongoClient
from bson import ObjectId 
from dotenv import load_dotenv
import os

load_dotenv()

mongo_url = os.getenv("MONGO_URL")

client = MongoClient(mongo_url, tlsAllowInvalidCertificates=True)

db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and time: {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count > 0:
            print("Video deleted successfully.")
        else:
            print("No video found with the given ID.")
    except Exception as e:
        print(f"An error occurred: {e}")


def  main():
    while True:
        print(" \n*** Youtube Manager Application ***\n")
        print("1. List of all Videos")
        print("2. Add a new Videos")
        print("3. Update a Videos")
        print("4. Delete a Videos")
        print("5. Exit the application")

        choice = input("Enter your Choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Which video you can update: ")
            name = input("Update the video name: ")
            time = input("update the time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the Id which video you want to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("Thanks to visit YTmanager application")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()