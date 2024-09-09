import requests
import logging

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f"The application is up. Status code: {response.status_code}")
            print("The application is up and running!")
        else:
            logging.warning(f"The application returned status code: {response.status_code}")
            print(f"Warning: The application returned status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to reach the application: {e}")
        print(f"Error: The application is down or not reachable. Details: {e}")

application_url = "https://www.example.com"

check_application_health(application_url)
