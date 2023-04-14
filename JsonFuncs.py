import json

def read_json_file(filename):
    """
    Reads data from a JSON file and returns it as a Python object.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def write_json_file(filename, data):
    """
    Writes data to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Read data from a JSON file
    data = read_json_file("/home/orangepi/Documents/Project/data.json")


    trigger = data["Counter"]
    trigger += 1
    data["Counter"] = trigger
    print(data["Counter"])

    # Write the modified data back to the JSON file
    write_json_file("/home/orangepi/Documents/Project/data.json", data)