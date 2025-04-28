# version_tracker.py

from datetime import datetime
import json
import os

VERSION_FILE = "versions.json"

def load_versions():
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_versions(versions):
    with open(VERSION_FILE, "w") as file:
        json.dump(versions, file, indent=4)

def add_version(version, title, description, contributors):
    versions = load_versions()
    new_version = {
        "version": version,
        "title": title,
        "description": description,
        "contributors": contributors,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    versions.append(new_version)
    save_versions(versions)
    print(f"Version {version} added successfully.")

def show_versions():
    versions = load_versions()
    if not versions:
        print("No versions recorded.")
        return

    print("\n=== Project Version History ===")
    for v in versions:
        print(f"\nVersion: {v['version']}")
        print(f"Title: {v['title']}")
        print(f"Description: {v['description']}")
        print(f"Contributors: {', '.join(v['contributors'])}")
        print(f"Timestamp: {v['timestamp']}")

if __name__ == "__main__":
    print("Welcome to the Note-Taking App Version Tracker")
    print("1. Add new version")
    print("2. Show all versions")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        version = input("Enter version (e.g. v1.0.0): ")
        title = input("Enter title of update: ")
        description = input("Enter description of update: ")
        contributors = input("Enter contributors (comma-separated): ").split(",")
        contributors = [c.strip() for c in contributors]
        add_version(version, title, description, contributors)
    elif choice == "2":
        show_versions()
    else:
        print("Invalid option. Exiting.")

#russell 
