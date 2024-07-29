# WebGuard

**WebGuard** is a security tool designed to scan websites for common vulnerabilities and security misconfigurations. It checks for SQL Injection, Cross-Site Scripting (XSS), missing security headers, open redirects, exposed sensitive files, and Cross-Site Request Forgery (CSRF) tokens.

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

