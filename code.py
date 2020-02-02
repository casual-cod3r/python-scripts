from tqdm import tqdm
from time import sleep

no_of_files = 5 #example
obj = tqdm(range(no_of_files))
for i in obj:
  obj.set_description(f'File uploading {i+1}:')
  sleep(1)
