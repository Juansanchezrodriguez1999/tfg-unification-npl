# NAME
Unified Names

# VERSION
1.0.0

# AUTHOR
Khaos Research Group

Juan Sánchez Rodríguez (juansanchezrodriguez1999@uma.es)

# DATE
14/10/2022

# DESCRIPTION
In the collection flora in mongoDB, the fields "Community", "Subcommunity" and "Community_Authors" and "Subcommunity_Authors" contain names that are sometimes misspelled, so, in this algorithm NLP techniques are used in order to unify all the equivalents names. For example, "Juan Sanchez". "Juan Sánchez", "Juan-Sánchez", "Juan-Sanchez" and "Jvam Sámches" are the same name but it has a little changes between them. In this algorithm this case is identified and repaired unifying all these names.
The unification of the names of the authors has not been possible, so the unified_authors function will not be executed at any time. The causes of this problem have been commented in a REPORT in the bitbucket task.

# INSTALLATION
First create a venv and then activate it. After that, run the following command:

```
pip install -r requirements.txt
```

## EXECUTION

```
python UnifiedNamesFlora.py --input_path "Json file path input with *.json extension" --output_path "Output path"

EXAMPLE: python UnifiedNamesFlora.py --input_path ~/*.json --output_path ~/folder1/folder2 

This example uses .json file path and the output path where output .json file is stored is folder2.

```

# PARAMETERS
* input_path (Path) --> .json file path.
* output_path (Path) --> Path of the new .json output file.


# OUTFILE
*.json file