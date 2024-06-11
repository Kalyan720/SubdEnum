import requests
from tqdm import tqdm
import time

def subdomain_enumeration():
    """
    Enumerate subdomains by checking predefined endpoints.

    Prompts the user for a base URL and checks the accessibility of predefined endpoints.

    """
    start_time = time.time()
    url = input("Enter the Domain that you wish to enumerate: ")
    try:
        with open('subdomains-100.txt', 'r') as file:
            data = file.read().splitlines()
            total_words = len(data)
            processed_words = 0
            subdomains_enumerated = []
            with tqdm(total=total_words, desc="Checking Subdomains", unit="word") as pbar:
                for word in data:
                    full_url = f"http://{word}.{url}"
                    print(f"Testing {full_url}")
                    try:
                        response = requests.get(full_url, timeout=10)
                        if response.status_code == 200:
                            subdomains_enumerated.append(full_url)
                        else:
                            continue
                    except requests.ConnectionError:
                        pass
                    except requests.exceptions.Timeout:
                        pass
                    except requests.exceptions.RequestException as e:
                        pass
                    processed_words += 1
                    pbar.update(1)
            print("\n")
            print(f"There are {len(subdomains_enumerated)} registered for the website")
            for i in subdomains_enumerated:
                print(i)
    except FileNotFoundError:
        print("Error: The subdomains file was not found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        end_time = time.time()
        run_time = end_time - start_time
        print(f"\nRuntime: {run_time} seconds")
if __name__ == "__main__":
    subdomain_enumeration()
