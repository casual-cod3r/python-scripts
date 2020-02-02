"""In this example, we will see how to code a progress bar for file upload using tqdm python module. Feel free to use it in your own way.

For more information, you may refer this docuentation - https://tqdm.github.io/

"""

from tqdm import tqdm # Importing tqdm module
from time import sleep # We are importing sleep() from time module to enter delay just for this example.

no_of_files = 5 # Example - 5 files to upload

""" Creating a TQDM object so that we can use it later to customize the progress bar. This line will loop through the given range i.e. number of files in this case """

obj = tqdm(range(no_of_files)) 

for i in obj: #iterating through object range to start the progress bar
  obj.set_description(f'File uploading {i+1}:')  
  sleep(1) # adding manual delay. This can be skipped for real example.
