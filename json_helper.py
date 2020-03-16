import json
import os
import pickle

def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.load(f)
    return data


def read_all_json_files(path):
    all_dicts = []
    for full_file in os.listdir(path):
        # full_filename = os.path.join(path, path, full_file)
        full_filename = os.path.join(path, full_file)
        with open(full_filename, 'r') as fi:
            dictionary = json.load(fi)
            all_dicts.append(dictionary)
    return all_dicts


def write_pickle(path, data):
    path = os.path.join(path, 'super_smash_characters.pickle')
    outfile = open(path, 'wb')
    pickle_one = pickle.dump(data, outfile, protocol=1)
    outfile.close()
    return pickle_one
    # print(pickle_one)


#
def load_pickle(pickle_one):
    path = open('super_smash_characters.pickle', 'wb')
    pickle.dumps(int(pickle_one), path)
    print(path)
#
write_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/', {
    "name": "Link",
    "neutral_special": "Bow and Arrows",
    "side_special": " Boomerang",
    "up_special": " Spin Attack",
    "down_special": "Remote Bomb",
    "final_smash": "Ancient Bow and Arrow"
})
# load_pickle('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
# read_json('/Users/rmaiale/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')
# read_all_json_files('/Users/rmaiale
# /dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
# opening = input("Please ")
