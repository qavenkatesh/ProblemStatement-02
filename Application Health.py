import requests
import psutil
import socket

def check_http_status(url):
    """Checks if a URL is reachable and returns the status code."""
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return None

def check_process_exists(process_name):
    """Checks if a process is running."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def check_port_open(host, port):
    """Checks if a port is open on a given host."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    # Replace with your application details
    app_url = "http://www.venkatesh.com"
    app_process = "gunicorn"  # Or "python app.py" if not using a process manager
    app_port = 8080

    # Perform health checks
    http_status = check_http_status(app_url)
    process_running = check_process_exists(app_process)
    port_open = check_port_open("localhost", app_port)

    # Print results
    print("Application Health Check:")
    print(f"HTTP Status: {http_status}")
    print(f"Process Running: {process_running}")
    print(f"Port Open: {port_open}")