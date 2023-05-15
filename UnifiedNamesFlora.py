import argparse
import json
from pathlib import Path

from Levenshtein import distance as lev


def unified_names_flora(json_file_path: Path, output_json_file_path: Path):
    """
    This function receives the input json file path and output path. 
    The json file input is converted to a list of dictionaries to access the keys:values.
    Then the values of the Community and Subcommunity keys are collected to unify the equivalent names. 
    Finally it returns a file in json format with the unified fields.
    :param json_file_path           --> json file path to load.
    :param output_json_file_path    --> output path where 'floras_unified.json' file with unified fields is stored.
    """
    with open(json_file_path, "r") as json_file:
        floras = json.load(json_file)
    # Here the function is executed to unify the values of "Community" and "Subcommunity"
    community_subcommunity_unification(floras, "Community", 5)
    community_subcommunity_unification(floras, "Subcommunity", 3)
    # Export new Json unified collection for mongoDB in output_json_file_path/floras_unified.json as explained in the example in README.md
    with open(
        str(output_json_file_path) + "/floras_unified.json", "w", encoding="utf-8"
    ) as output_json_file:
        json.dump(floras, output_json_file, indent=1, ensure_ascii=False)


def community_subcommunity_unification(
    json_list: list[dict[str, any]], key: str, distance: int
) -> None:
    """
    This function receives a list of dictionaries, keys to be unified and Lev distance.
    :param json_list:   list of dictionaries (list).
    :param key:         keys that have to be unified (string).
    :param distance:    Levenshtein distance (integer).
    """
    community = []
    for i in range(0, len(json_list)):
        if json_list[i][key] != None:
            community.append(json_list[i][key])
    # Make a dictionary of community occurrences and repetitions
    frecuency_community = [community.count(p) for p in community]
    dict_community = dict(list(zip(community, frecuency_community)))
    list_dict_community_keys = sorted(list(dict_community.keys()))
    # Find community equivalents and select the highest frequency
    for i in range(0, len(json_list)):
        if json_list[i][key] != None:
            for j in range(0, len(list_dict_community_keys)):
                dist = lev(json_list[i][key], list_dict_community_keys[j])
                if (
                    dist < distance
                    and dist != 0
                    and dict_community[json_list[i][key]]
                    < dict_community[list_dict_community_keys[j]]
                    and list_dict_community_keys[j]
                    != "Scrophulario laxiflorae-Rhododendretum pontici"
                    and list_dict_community_keys[j] != "Chenopodietum muralis"
                ):
                    json_list[i][key] = list_dict_community_keys[j]


def unified_authors(json_list: list[dict[str, any]], key1: str, key2: str) -> None:
    """
    This function will not be executed at any time due to problems with the unification of names.
    This function receives a list of dictionaries (each one belongs to a species), it also receives two keys that will be unified in the same key.
    :param key1: Key to be merged with key2 (string).
    :param key2: Key to be merged with key1 (string).
    """
    community_subcommunity_authors = []
    for i in range(0, len(json_list)):
        community_subcommunity_authors.append(
            json_list[i]["key1"] + json_list[i]["key2"]
        )
    # The unification of the authors has not been possible due to the circumstances shown in the report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=Path, help=".json file path", required=True)
    parser.add_argument("--output_path", type=Path, help="Output file path", required=True)
    args = parser.parse_args()
    if args.input_path.is_file() and args.input_path.name.endswith(".json"):
        if args.output_path.is_dir():
            unified_names_flora(args.input_path, args.output_path)
        else:
            print(
                "'--output_path' must be a path where output json file (floras_unified.json) is stored."
            )
    else:
        print("'--input_path' must be json file path with extension .json.")

