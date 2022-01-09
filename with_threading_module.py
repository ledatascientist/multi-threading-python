import threading
import time
import requests as r

BASE_URL='https://archive.ics.uci.edu/ml/datasets'
URLS = [ f'{BASE_URL}/Energy+efficiency',f'{BASE_URL}/Planning+Relax',f'{BASE_URL}/Cloud',
f'{BASE_URL}/Protein+Data',f'{BASE_URL}/Spambase'] *3

def get_dataset (url):
    response = r.get(url)
    print( f"Got data form {url}: content length: {len(response.content)}")


if __name__ == "__main__":
    start = time.perf_counter()
    threads = []
    for url in URLS:
        t = threading.Thread(target=get_dataset, args=(url,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    #get_dataset (URLS)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    #2 seconds