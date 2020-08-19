import requests

# downlaod file
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

# raise an exception if there is a connection error
# res = requests.get('http://blahlskdikakadoesnotworkdoesnotwork')
# res.raise_for_status()

# save content to computer using write-binary mode to maintain the unicode enconding of the text
# to learn more: http://bit.ly/unipain
playFile = open('romeoAndJuliet.txt', 'wb')

# use iter_content() to write chunk by chunk so that you don't put too much data in memory
# in the code below, we break apart the res object in chunks of 100,000 bites and iterated
# through the entire response object
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close