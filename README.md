
# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-124-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--09--13-orange) ![Level](https://img.shields.io/badge/Level-NEWBIE-green) ![Vulnerability labs](https://img.shields.io/badge/completed-42%25-purple)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

## Level progress
- **Apprentice**: 40 of 61
- **Practitioner**: 80 of 174
- **Expert**: 6 of 39

## Categories Covered

- **Authentication vulnerabilities**: 14/14 labs
- **SQL injection**: 8/18 lab
- **Path Traversal**: 6/6
- **Cross-site scripting** 16/31
- **Command injection**:5/5
- **Server-side request forgery (SSRF)**: 7/7
- **Web cache poisoning**: 9/13
- **Access control**: 13/13 lab
- **Business logic vulnerabilities**: 6/6
- **File upload vulnerabilities**: 6/7
- **JWT**:6/8
- **Race conditions**: 6/7
- **Cross-site request forgery (CSRF)**: 6/14
- **Server-side template injection**: 3/7
- **API testing**: 5/5
- **HTTP request smuggling**: 5/22
- **XML external entity (XXE) injection**: 4/9
  
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
| 76 | 2026-07-13 | File upload vulnerabilities | Remote code execution via web shell upload | apprentice | N/A |
| 77 | 2026-07-13 | File upload vulnerabilities | Web shell upload via Content-Type restriction bypass | apprentice | N/A |
| 78 | 2026-07-13 | File upload vulnerabilities | Web shell upload via path traversal | practitioner | N/A |
| 79 | 2026-07-14 | File upload vulnerabilities | Web shell upload via extension blacklist bypass | practitioner | N/A |
| 80 | 2026-07-14 | File upload vulnerabilities | Web shell upload via obfuscated file extension | practitioner | N/A |
| 81 | 2026-07-14 | File upload vulnerabilities | Remote code execution via polyglot web shell upload | practitioner | N/A |
| 82 | 2026-07-15 | JWT | JWT authentication bypass via unverified signature | apprentice | N/A |
| 83 | 2026-07-15 | JWT | JWT authentication bypass via flawed signature verification | apprentice | N/A |
| 84 | 2026-07-16 | JWT | JWT authentication bypass via weak signing key | practitioner | N/A |
| 85 | 2026-07-16 | JWT | JWT authentication bypass via jwk header injection | practitioner | N/A |
| 86 | 2026-07-17 | JWT | JWT authentication bypass via jku header injection | practitioner | N/A |
| 87 | 2026-07-18 | JWT | JWT authentication bypass via kid header path traversal | practitioner | N/A |
| 88 | 2026-07-20 | Race conditions | Limit overrun race conditions | apprentice | N/A |
| 89 | 2026-07-20 | Race conditions | Bypassing rate limits via race conditions | practitioner | N/A |
| 90 | 2026-07-21 | Race conditions | Multi-endpoint race conditions | practitioner | N/A |
| 91 | 2026-07-22 | Race conditions | Single-endpoint race conditions | practitioner | N/A |
| 92 | 2026-07-23 | Race conditions | Exploiting time-sensitive vulnerabilities | practitioner | N/A |
| 93 | 2026-07-25 | Race conditions | Partial construction race conditions | expert | N/A |
| 94 | 2026-07-27 | Cross-site request forgery (CSRF) | CSRF vulnerability with no defenses | apprentice | N/A |
| 95 | 2026-07-27 | Cross-site request forgery (CSRF) | CSRF where token validation depends on request method | practitioner | N/A |
| 96 | 2026-07-28 | Cross-site request forgery (CSRF) | CSRF where token validation depends on token being present | practitioner | N/A |
| 97 | 2026-07-28 | Cross-site request forgery (CSRF) | CSRF where token is not tied to user session | practitioner | N/A |
| 98 | 2026-07-29 | Cross-site request forgery (CSRF) | CSRF where token is tied to non-session cookie | practitioner | N/A |
| 99 | 2026-08-29 | Cross-site request forgery (CSRF) | CSRF where token is duplicated in cookie | practitioner | N/A |
| 100 | 2026-08-01 | Server-side template injection | Basic server-side template injection | practitioner | N/A |
| 101 | 2026-08-01 | Server-side template injection | Basic server-side template injection (code context) | practitioner | N/A |
| 102 | 2026-08-01 | Server-side template injection | Server-side template injection using documentation | practitioner | N/A |
| 103 | 2026-08-03 | API testing | Exploiting an API endpoint using documentation | apprentice | N/A |
| 104 | 2026-08-03 | API testing | Exploiting server-side parameter pollution in a query string | practitioner | N/A |
| 105 | 2026-08-04 | API testing | Finding and exploiting an unused API endpoint | practitioner | N/A |
| 106 | 2026-08-05 | API testing | Exploiting a mass assignment vulnerability | practitioner | N/A |
| 107 | 2026-08-08 | API testing | Exploiting server-side parameter pollution in a REST URL | expert | N/A |
| 108 | 2026-08-12 | Cross-site scripting | Reflected XSS into attribute with angle brackets HTML-encoded | apprentice | N/A |
| 109 | 2026-08-12 | Cross-site scripting | Stored XSS into anchor href attribute with double quotes HTML-encoded | apprentice | N/A |
| 110 | 2026-08-13 | Cross-site scripting | Reflected XSS into a JavaScript string with angle brackets HTML encoded | apprentice | N/A |
| 111 | 2026-08-13 | Cross-site scripting | DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded | practitioner | N/A |
| 112 | 2026-08-14 | Cross-site scripting | Reflected DOM XSS | practitioner | N/A |
| 113 | 2026-08-14 | Cross-site scripting | Stored DOM XSS | practitioner | N/A |
| 114 | 2026-08-15 | Cross-site scripting | Reflected XSS into HTML context with all tags blocked except custom ones | practitioner | N/A |
| 115 | 2026-08-15 | Cross-site scripting | Reflected XSS with some SVG markup allowed | practitioner | N/A |
| 116 | 2026-08-25 | HTTP request smuggling | HTTP request smuggling, confirming a CL.TE vulnerability via differential responses | practitioner | N/A |
| 117 | 2026-08-25 | HTTP request smuggling | HTTP request smuggling, confirming a TE.CL vulnerability via differential responses | practitioner | N/A |
| 118 | 2026-08-26 | HTTP request smuggling | Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability | practitioner | N/A |
| 119 | 2026-08-26 | HTTP request smuggling | Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability | practitioner | N/A |
| 120 | 2026-08-26 | HTTP request smuggling | Exploiting HTTP request smuggling to reveal front-end request rewriting | practitioner | N/A |
| 121 | 2026-09-10 | XML external entity (XXE) injection | Exploiting XXE using external entities to retrieve files | apprentice | N/A |
| 122 | 2026-09-10 | XML external entity (XXE) injection | Exploiting XXE to perform SSRF attacks | apprentice | N/A |
| 123 | 2026-09-12 | XML external entity (XXE) injection | Blind XXE with out-of-band interaction | practitioner | N/A |
| 124 | 2026-09-12 | XML external entity (XXE) injection | Blind XXE with out-of-band interaction via XML parameter entities | practitioner | N/A |
=======
