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
            subdomains_enumerated = []
            
            with tqdm(total=total_words, desc="Checking Subdomains", unit="word") as pbar:
                for word in data:
                    full_url = f"http://{word}.{url}"
                    try:
                        response = requests.get(full_url, timeout=10)
                        if response.status_code == 200:
                            subdomains_enumerated.append(full_url)
                    except requests.ConnectionError:
                        # Log connection error (e.g., domain doesn't exist)
                        pass
                    except requests.exceptions.Timeout:
                        # Log timeout (e.g., server too slow or not responding)
                        pass
                    except requests.exceptions.RequestException as e:
                        # Log other request exceptions
                        print(f"Error occurred: {e}")
                    
                    pbar.update(1)
            
            print("\n")
            print(f"{len(subdomains_enumerated)} subdomains registered for the website:")
            for subdomain in subdomains_enumerated:
                print(subdomain)
    
    except FileNotFoundError:
        print("Error: The subdomains file was not found.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        end_time = time.time()
        run_time = end_time - start_time
        print(f"\nRuntime: {run_time:.2f} seconds")

if __name__ == "__main__":
    subdomain_enumeration()
