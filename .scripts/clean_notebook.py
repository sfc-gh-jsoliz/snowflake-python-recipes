import glob
import json
filelist = glob.glob("*/*.ipynb")
for filename in filelist: 
    notebooks = json.load(open(filename,'r'))
    # Remove lastEditStatus if it exists
    notebooks.get("metadata", {}).pop("lastEditStatus", None)
    # Rename all cell number
    i=1
    for cell in notebooks["cells"]: 
        cell["metadata"]["name"] = f"cell{i}"
        i+=1
    json.dump(notebooks, open(f"{filename}",'w'), indent=2)
    print(f"Updated {filename}")
