# WebGuard

**WebGuard** is a security tool designed to scan websites for common vulnerabilities and security misconfigurations. It checks for SQL Injection, Cross-Site Scripting (XSS), missing security headers, open redirects, exposed sensitive files, and Cross-Site Request Forgery (CSRF) tokens.

## Banner

![WebGuard Banner](https://github.com/Guman-Rajpurohit/WebGuard/blob/main/Banner.png?raw=true)

## Features

- **SQL Injection**: Detects if the website is vulnerable to SQL injection.
- **Cross-Site Scripting (XSS)**: Checks if the website is vulnerable to XSS attacks.
- **Security Headers Check**: Verifies the presence of essential security headers.
- **Open Redirect**: Identifies potential open redirect vulnerabilities.
- **Sensitive Files Exposure**: Scans for exposed sensitive files on the server.
- **Cross-Site Request Forgery (CSRF) Tokens**: Finds hidden CSRF tokens in forms.

## Installation

To install the necessary dependencies, run:

```sh
pip install requests beautifulsoup4 lxml
```
## Usage
To use WebGuard, run the following command in your terminal:
```sh
python webguard.py
```
When prompted, enter the URL of the website you want to scan. The script will check for various vulnerabilities and print the results.
## Example Output

```yaml
Enter the URL to scan: http://example.com

Scanning http://example.com for vulnerabilities...

[!] SQL Injection vulnerability detected.
[-] No XSS vulnerability found.
[!] Missing security headers: X-Frame-Options, X-XSS-Protection
[-] No open redirect vulnerability found.
[!] Exposed sensitive files: http://example.com/.env, http://example.com/config.php
[!] CSRF tokens found: abc123, def456

```
## Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool on websites you do not own or have explicit permission to test is illegal and unethical. Always obtain proper authorization before conducting security tests.

