import concurrent.futures
import time
import requests as r



BASE_URL='https://archive.ics.uci.edu/ml/datasets'
URLS = [ f'{BASE_URL}/Energy+efficiency',f'{BASE_URL}/Planning+Relax',f'{BASE_URL}/Cloud',
f'{BASE_URL}/Protein+Data',f'{BASE_URL}/Spambase'] *3

def get_dataset (url:str):
    response = r.get(url)
    print( f"Got data form {url}: content length: {len(response.content)}")


if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_dataset, URLS)
    #get_dataset (URLS)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    #3 seconds