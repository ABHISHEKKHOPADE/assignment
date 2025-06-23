import os
from pathlib import Path

project_name = "project"

list_of_files = [

    f"{project_name}/data",
    f"{project_name}/analysis.ipynb",

    
    f"{project_name}/sentiment_trade_analysis.py",  
    
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")