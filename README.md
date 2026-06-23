
# PortSwigger Web Security Academy - Solved Labs

![Total Labs](https://img.shields.io/badge/Total%20Labs%20Solved-13-blue) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--06--23-yellow) ![Level](https://img.shields.io/badge/Level-NEWBIE-green) ![Vulnerability labs](https://img.shields.io/badge/Completed-0%25-purple)

This file tracks my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security) labs. I focus on web app pentesting, documenting key labs as full writeups (linked below) and logging all solves here for reference. Full writeups are reserved for first-time techniques, complex exploits, or custom tools.

## Level progress
- **Apprentice**: 5 of 61
- **Practitioner**: 7of 174
- **Expert**: 0 of 39

## Categories Covered

- **Authentication vulnerabilities**: 5/14 lab
- **SQL injection**: 8/18 lab
- **Access control**: 0/13 lab

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

=======
