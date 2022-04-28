import json
import tqdm

path = "gutenberg-poetry-v001.ndjson"

outpath = "poetry"

out = open(outpath, "w")

for line in tqdm.tqdm(open(path,'r').readlines()):
	out.write(json.loads(line)["s"]+ "\n")
	
