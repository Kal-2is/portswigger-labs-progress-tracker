# Lab: Username Enumeration via Response Timing

This lab demonstrates how to enumerate valid usernames by measuring differences in the application's response time. The lab also introduces bypassing IP-based rate limiting using the `X-Forwarded-For` header.

---

## Lab Objective

- Enumerate a valid username using response timing.
- Bypass IP blocking.
- Brute-force the user's password.
- Log in to solve the lab.

---

## Username List

<details>
<summary>Click to expand</summary>

```text
carlos
root
admin
test
guest
info
adm
mysql
user
administrator
oracle
ftp
pi
puppet
ansible
ec2-user
vagrant
azureuser
academico
acceso
access
accounting
accounts
acid
activestat
ad
adam
adkit
admin
administracion
administrador
administrator
administrators
admins
ads
adserver
adsl
ae
af
affiliate
affiliates
afiliados
ag
agenda
agent
ai
aix
ajax
ak
akamai
al
alabama
alaska
albuquerque
alerts
alpha
alterwind
am
amarillo
americas
an
anaheim
analyzer
announce
announcements
antivirus
ao
ap
apache
apollo
app
app01
app1
apple
application
applications
apps
appserver
aq
ar
archie
arcsight
argentina
arizona
arkansas
arlington
as
as400
asia
asterix
at
athena
atlanta
atlas
att
au
auction
austin
auth
auto
autodiscover
```

</details>

---

## Password List

<details>
<summary>Click to expand</summary>

```text
123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
superman
1qaz2wsx
7777777
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
mobilemail
mom
monitor
monitoring
montana
moon
moscow
```

</details>

---

# Initial Observation

After launching the lab, I first examined the login page.

<p align="center">
<img src="./assets for username enumration write up/login page.png" width="700">
</p>

I manually tested several username and password combinations. After a few failed attempts, the application blocked my IP address.

<p align="center">
<img src="./assets for username enumration write up/the requests.png" width="700">
</p>

---

# Bypassing the Rate Limit

The application trusts the `X-Forwarded-For` header. By supplying a different IP address in this header for every request, the rate limit can be bypassed.

Example:

```http
X-Forwarded-For: 1
```

To verify this, I sent the request to **Burp Repeater** and modified the header.

<p align="center">
<img src="./assets for username enumration write up/check x-forward-for.png" width="700">
</p>

The request was accepted, confirming that the application trusts the supplied `X-Forwarded-For` value.

---

# Identifying a Valid Username

While testing different usernames, I noticed an important behavior.

For an **invalid username**, the response time remained nearly constant regardless of the password length.

For a **valid username**, the response time increased when a longer password was supplied.

Short password:

<p align="center">
<img src="./assets for username enumration write up/shortpassword.png" width="700">
</p>

Long password:

<p align="center">
<img src="./assets for username enumration write up/longpassword.png" width="700">
</p>

This timing difference can be used to identify valid usernames.

---

# Enumerating the Username

Send the request to **Burp Intruder**.

Select the **Pitchfork** attack type because two payload positions are required:

- Payload 1 → `X-Forwarded-For`
- Payload 2 → Username

Configure the payloads as shown below.

### Payload 1 - X-Forwarded-For

<p align="center">
<img src="./assets for username enumration write up/payload for x-forward.png" width="700">
</p>

### Payload 2 - Username List

<p align="center">
<img src="./assets for username enumration write up/forusernamepayload.png" width="700">
</p>

Start the attack.

The username with the noticeably longer response time is the valid account.

<p align="center">
<img src="./assets for username enumration write up/theresultofusername.png" width="700">
</p>

**Discovered username**

```text
archie
```

---

# Brute-Forcing the Password

Now that the valid username is known, repeat the same process.

Keep the `X-Forwarded-For` payload to bypass rate limiting, but replace the username payload with the password list.

<p align="center">
<img src="./assets for username enumration write up/thepasswordpayload.png" width="700">
</p>

Launch the attack again.

The successful response identifies the correct password.

<p align="center">
<img src="./assets for username enumration write up/correctpassword.png" width="700">
</p>

**Discovered password**

```text
starwars
```

---

# Login

Log in using the discovered credentials.

| Username | Password |
|----------|----------|
| `archie` | `starwars` |

After authentication, the lab is successfully solved.

<p align="center">
<img src="./assets for username enumration write up/solved.png" width="700">
</p>

---

# Summary

This lab demonstrated:

- Detecting valid usernames using response timing.
- Bypassing IP-based rate limiting with the `X-Forwarded-For` header.
- Using Burp Intruder's **Pitchfork** attack.
- Enumerating a valid username.
- Brute-forcing the corresponding password.
- Successfully authenticating and completing the lab.