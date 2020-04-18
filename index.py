import os
import json
from ffprobe_analyze import collect_info


def do_index(index_path, anime_path, simulation_mode):
    json_data = {}
    with open(index_path, 'w') as f:
        # traverse dir
        for root, dirs, files in os.walk(anime_path):
            if root == anime_path:
                print("Anime:", len(dirs))
            if "Season 01" in dirs:
                anime_name = root.split("\\")
                anime_name = anime_name[-1]
                seasons = len(dirs)
                print(f"{anime_name} with {seasons} seasons")
            if "Season" in root:
                season = root.split("\\")
                season = season[-1]
                size = 0
                folge = 0
                if not simulation_mode:
                    for file in files:
                        if "txt" not in file:
                            print(file)
                            folge += 1
                            size = round(os.path.getsize(root + '\\' + file) / 1000000)
                            if anime_name in json_data:
                                if season not in json_data[anime_name]:
                                    json_data[anime_name].append(season)
                                    json_data[anime_name].append({folge: collect_info(root + '\\' + file, size)})
                                else:
                                    json_data[anime_name].append({folge: collect_info(root + '\\' + file, size)})
                            else:
                                json_data[anime_name] = []
                                json_data[anime_name].append(season)
                                json_data[anime_name].append({folge: collect_info(root + '\\' + file, size)})
                        else:
                            json_data = {}
        json.dump(json_data, f, indent=4, ensure_ascii=False)

# do_index(index_path, anime_path)
