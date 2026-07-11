
# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-75-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--07--11-yellow) ![Level](https://img.shields.io/badge/Level-NEWBIE-green) ![Vulnerability labs](https://img.shields.io/badge/completed-20%25-purple)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

## Level progress
- **Apprentice**: 28 of 61
- **Practitioner**: 44 of 174
- **Expert**: 4 of 39

## Categories Covered

- **Authentication vulnerabilities**: 14/14 labs
- **SQL injection**: 8/18 lab
- **Path Traversal**: 6/6
- **Cross-site scripting** 7/31
- **Command injection**:5/5
- **Server-side request forgery (SSRF)**: 7/7
- **Web cache poisoning**: 9/13
- **Access control**: 13/13 lab
- **Business logic vulnerabilities**: 6/6
  
## Notes
- **Full Writeups**: Only for significant labs (e.g., chained exploits or scripted solutions). See `platforms/portswigger/` for details.
- **Tools Used**: Burp Suite

## How to Read
- **Columns**: 
  - `No`: Sequential lab number.
  - `Date`: When I solved it (YYYY-MM-DD).
  - `Topic`: Vulnerability category (e.g., API Testing, XSS).
  - `Lab Title`: Exact name from PortSwigger.
  - `Difficulty`: Apprentice, Practitioner, or Expert.
  - `Writeup Link`: Links to full writeup (if exists) or "N/A" for quick solves.

---

## Solved Labs

| No | Date          | Topic            | Lab Title                                   | Difficulty  | Writeup Link |
|----|------------|----------------|---------------------------------------------|-------------|--------------|
| 1  | 2026-06-16 |      Sql injection          | SQL injection attack, querying the database type and version on Oracle      |       practitioner      | <a href="assets/SQL Injection Attack - Querying the Database Type and Version on Oracle.md">this</a>|
| 2  | 2026-06-17 |      Sql injectioin          |      SQL injection vulnerability in WHERE clause allowing retrieval of hidden data  |    apprentice         | N/A          |
| 3  | 2026-06-17 |       Sql injection         |  SQL injection vulnerability allowing login bypass |       apprentice      | N/A          |
| 4  | 2026-06-17 |  Sql injection |  SQL injection attack, querying the database type and version on Oracle   |    apprentice   | N/A          |
| 5  | 2026-06-18 |   Sql injection  |   SQL injection attack, querying the database type and version on MySQL and Microsoft   |    practitioner         | N/A          |
|6 | 2026-06-18| Sql injection | SQL injection attack, listing the database contents on non-Oracle databases| practitioner|N/A|
|7 | 2026-06-18| Sql injection | SQL injection attack, listing the database contents on Oracle| practitioner|N/A|
|8| 2026-06-20 | Sql injection | SQL injection UNION attack, determining the number of columns returned by the query|practitioner|N/A|
| 9  | 2026-06-23 | Autherntication | Username enumeration via different responses | apprentice         |N/A|
| 10  | 2026-06-23 | Autherntication | 2FA simple bypass | apprentice         |N/A|
| 11 | 2026-06-23 | Autherntication | Password reset broken logic | apprentice         |N/A|
| 12 | 2026-06-23 | Autherntication | Username enumeration via subtly different responses | practitioner |N/A|
| 13 | 2026-06-23 | Autherntication | Username enumeration via response timing| practitioner |<a href="./assets/Username enumeration via response timing.md">here</a>|
| 14 | 2026-06-24 | Autherntication | Broken brute-force protection, IP block | practitioner |<a href="./assets/broken1.md">here</a>|
| 15| 2026-06-24 | Autherntication |Username enumeration via account lock| practitioner |N/A|
| 16  | 2026-06-25 | Autherntication | 2FA broken logic | apprentice         |N/A|
| 17  | 2026-06-25 | Autherntication | Brute-forcing a stay-logged-in cookie | apprentice         |N/A|
| 18 | 2026-06-25 | Autherntication |Offline password cracking | apprentice         |N/A|
| 19 | 2026-06-26 | Autherntication | Password reset poisoning via middleware | apprentice         |N/A|
| 20 | 2026-06-26 | Autherntication | Password brute-force via password change | apprentice         |N/A|
| 21 | 2026-06-26 | Autherntication | Broken brute-force protection, multiple credentials per request | apprentice         |N/A|
| 22 | 2026-06-26 | Authentication | 2FA bypass using a brute-force attack | apprentice | N/A |
| 23 | 2026-06-29| Path traversal | File path traversal, simple case | apprentice | N/A |
| 24 | 2026-06-29 | Path traversal | File path traversal, traversal sequences blocked with absolute path bypass | practitioner | N/A |
| 25 | 2026-07-01 | Path traversal | File path traversal, traversal sequences stripped non-recursively | practitioner | N/A |
| 26 | 2026-07-01 | Path traversal | File path traversal, traversal sequences stripped with superfluous URL-decode | practitioner | N/A |
| 27 | 2026-07-01 | Path traversal | File path traversal, validation of start of path | practitioner | N/A |
| 28 | 2026-07-01 | Path traversal | File path traversal, validation of file extension with null byte bypass | practitioner | N/A |
| 29 | 2026-07-03 | Cross-site scripting | Reflected XSS into HTML context with nothing encoded | apprentice | N/A |
| 30 | 2026-07-03 | Cross-site scripting | Stored XSS into HTML context with nothing encoded | apprentice | N/A |
| 31 | 2026-07-03 | Cross-site scripting | DOM XSS in document.write sink using source location.search | apprentice | N/A |
| 32 | 2026-07-03 | Cross-site scripting | DOM XSS in innerHTML sink using source location.search | apprentice | N/A |
| 33 | 2026-07-03 | Cross-site scripting | DOM XSS in jQuery anchor href attribute sink using location.search source | apprentice | N/A |
| 34 | 2026-07-03 | Cross-site scripting | DOM XSS in jQuery selector sink using a hashchange event | apprentice | N/A |
| 35 | 2026-07-03 | Cross-site scripting | DOM XSS in document.write sink using source location.search inside a select element | practitioner | N/A |
| 36 | 2026-07-04 | Web cache poisoning | Web cache poisoning with an unkeyed header | practitioner | N/A |
| 37 | 2026-07-04 | Web cache poisoning | Web cache poisoning with an unkeyed cookie | practitioner | N/A |
| 38 | 2026-07-04 | Web cache poisoning | Web cache poisoning with multiple headers | practitioner | N/A |
| 39 | 2026-07-04 | Web cache poisoning | Targeted web cache poisoning using an unknown header | practitioner | N/A |
| 40 | 2026-07-04 | Web cache poisoning | Web cache poisoning via an unkeyed query string | practitioner | N/A |
| 41 | 2026-07-04 | Web cache poisoning | Web cache poisoning via an unkeyed query parameter | practitioner | N/A |
| 42 | 2026-07-04 | Web cache poisoning | Parameter cloaking | practitioner | N/A |
| 43 | 2026-07-04 | Web cache poisoning | Web cache poisoning via a fat GET request | practitioner | N/A |
| 44 | 2026-07-04 | Web cache poisoning | URL normalization | practitioner | N/A |
| 45 | 2026-07-05 | OS command injection | OS command injection, simple case | apprentice | N/A |
| 46 | 2026-07-05 | OS command injection | Blind OS command injection with time delays | practitioner | N/A |
| 47 | 2026-07-05 | OS command injection | Blind OS command injection with output redirection | practitioner | N/A |
| 48 | 2026-07-05 | OS command injection | Blind OS command injection with out-of-band interaction | practitioner | N/A |
| 49 | 2026-07-05 | OS command injection | Blind OS command injection with out-of-band data exfiltration | practitioner | N/A |
| 50 | 2026-07-05 | Server-side request forgery (SSRF) | Basic SSRF against the local server | apprentice | N/A |
| 51 | 2026-07-05 | Server-side request forgery (SSRF) | Basic SSRF against another back-end system | apprentice | N/A |
| 52 | 2026-07-05 | Server-side request forgery (SSRF) | Blind SSRF with out-of-band detection | practitioner | N/A |
| 53 | 2026-07-05 | Server-side request forgery (SSRF) | SSRF with blacklist-based input filter | practitioner | N/A |
| 54 | 2026-07-05 | Server-side request forgery (SSRF) | SSRF with filter bypass via open redirection vulnerability | practitioner | N/A |
| 55 | 2026-07-05 | Server-side request forgery (SSRF) | Blind SSRF with Shellshock exploitation | expert | N/A |
| 56 | 2026-07-05 | Server-side request forgery (SSRF) | SSRF with whitelist-based input filter | expert | N/A |
| 57 | 2026-07-07 | Access control vulnerabilities | Unprotected admin functionality | apprentice | N/A |
| 58 | 2026-07-07 | Access control vulnerabilities | Unprotected admin functionality with unpredictable URL | apprentice | N/A |
| 59 | 2026-07-07 | Access control vulnerabilities | User role controlled by request parameter | apprentice | N/A |
| 60 | 2026-07-07 | Access control vulnerabilities | User role can be modified in user profile | apprentice | N/A |
| 61 | 2026-07-07 | Access control vulnerabilities | User ID controlled by request parameter | apprentice | N/A |
| 62 | 2026-07-07 | Access control vulnerabilities | User ID controlled by request parameter, with unpredictable user IDs | apprentice | N/A |
| 63 | 2026-07-07 | Access control vulnerabilities | User ID controlled by request parameter with data leakage in redirect | apprentice | N/A |
| 64 | 2026-07-08 | Access control vulnerabilities | User ID controlled by request parameter with password disclosure | apprentice | N/A |
| 65 | 2026-07-08 | Access control vulnerabilities | Insecure direct object references | apprentice | N/A |
| 66 | 2026-07-08 | Access control vulnerabilities | URL-based access control can be circumvented | practitioner | N/A |
| 67 | 2026-07-08 | Access control vulnerabilities | Method-based access control can be circumvented | practitioner | N/A |
| 68 | 2026-07-09 | Access control vulnerabilities | Multi-step process with no access control on one step | practitioner | N/A |
| 69 | 2026-07-09 | Access control vulnerabilities | Referer-based access control | practitioner | N/A |
| 70 | 2026-07-10 | Business logic vulnerabilities | Excessive trust in client-side controls | apprentice | N/A |
| 71 | 2026-07-10 | Business logic vulnerabilities | High-level logic vulnerability | apprentice | N/A |
| 72 | 2026-07-10 | Business logic vulnerabilities | Inconsistent security controls | apprentice | N/A |
| 73 | 2026-07-11 | Business logic vulnerabilities | Flawed enforcement of business rules | apprentice | N/A |
| 74 | 2026-07-11 | Business logic vulnerabilities | Low-level logic flaw | practitioner | N/A |
| 75 | 2026-07-11 | Business logic vulnerabilities | Inconsistent handling of exceptional input | practitioner | N/A |

=======
