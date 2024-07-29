import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time  # Import time module to use sleep

# ANSI escape sequences for styling
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def is_vulnerable_to_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url, params={'id': payload})
    return payload in response.text

def is_vulnerable_to_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={'q': payload})
    return payload in response.text

def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    missing_headers = []

    if 'X-Frame-Options' not in headers:
        missing_headers.append('X-Frame-Options')

    if 'X-XSS-Protection' not in headers:
        missing_headers.append('X-XSS-Protection')

    if 'X-Content-Type-Options' not in headers:
        missing_headers.append('X-Content-Type-Options')

    if 'Strict-Transport-Security' not in headers:
        missing_headers.append('Strict-Transport-Security')

    return missing_headers

def is_vulnerable_to_open_redirect(url):
    payload = "http://evil.com"
    response = requests.get(url, params={'next': payload})
    return payload in response.url

def check_sensitive_files(url):
    sensitive_paths = [
        'robots.txt', '.git/', '.env', 'config.php', 'admin/', 'backup/', 'wp-config.php'
    ]
    exposed_files = []

    for path in sensitive_paths:
        full_url = urljoin(url, path)
        response = requests.get(full_url)
        if response.status_code == 200:
            exposed_files.append(full_url)

    return exposed_files

def find_csrf_tokens(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tokens = []

    for form in soup.find_all('form'):
        inputs = form.find_all('input')
        for input_tag in inputs:
            if input_tag.get('type') == 'hidden' and 'token' in input_tag.get('name', '').lower():
                tokens.append(input_tag['value'])

    return tokens

def main():
    # Display the styled ASCII art title with delay
    title_lines = [
        "██     ██ ███████ ██████   ██████  ██    ██  █████  ██████  ██████  ",
        "██     ██ ██      ██   ██ ██       ██    ██ ██   ██ ██   ██ ██   ██ ",
        "██  █  ██ █████   ██████  ██   ███ ██    ██ ███████ ██████  ██   ██ ",
        "██ ███ ██ ██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██   ██ ",
        " ███ ███  ███████ ██████   ██████   ██████  ██   ██ ██   ██ ██████  ",
        "                                                                    ",
        "                     By Guman Rajpurohit                                  ",
        "                                                                    ",
        "                         Follow For More                            ",
        "                      https://bit.ly/4c1viyE                        ",
        "                                                                    ",
        "                                                                    "
    ]

    print(f"{CYAN}{BOLD}")
    for line in title_lines:
        print(line)
        time.sleep(0.1)  # Pause for 0.1 seconds between each line
    print(RESET)

    url = input("Enter the URL to scan: ").strip()
    url = url if url.startswith('http') else 'http://' + url

    print(f"\nScanning {url} for vulnerabilities...\n")

    if is_vulnerable_to_sql_injection(url):
        print(f"{RED}[!] SQL Injection vulnerability detected.{RESET}")
    else:
        print(f"{GREEN}[-] No SQL Injection vulnerability found.{RESET}")

    if is_vulnerable_to_xss(url):
        print(f"{RED}[!] XSS vulnerability detected.{RESET}")
    else:
        print(f"{GREEN}[-] No XSS vulnerability found.{RESET}")

    missing_headers = check_security_headers(url)
    if missing_headers:
        print(f"{YELLOW}[!] Missing security headers: {', '.join(missing_headers)}{RESET}")
    else:
        print(f"{GREEN}[-] All essential security headers are present.{RESET}")

    if is_vulnerable_to_open_redirect(url):
        print(f"{RED}[!] Open redirect vulnerability detected.{RESET}")
    else:
        print(f"{GREEN}[-] No open redirect vulnerability found.{RESET}")

    exposed_files = check_sensitive_files(url)
    if exposed_files:
        print(f"{YELLOW}[!] Exposed sensitive files: {', '.join(exposed_files)}{RESET}")
    else:
        print(f"{GREEN}[-] No sensitive files exposed.{RESET}")

    csrf_tokens = find_csrf_tokens(url)
    if csrf_tokens:
        print(f"{YELLOW}[!] CSRF tokens found: {', '.join(csrf_tokens)}{RESET}")
    else:
        print(f"{GREEN}[-] No CSRF tokens found in forms.{RESET}")

if __name__ == "__main__":
    main()

