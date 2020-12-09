import json
with open('testj.json')as f:
    data = json.load(f)
    data["grades"]=[0,0,0,0,0]
open("testj.json", "w").write(
        json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))