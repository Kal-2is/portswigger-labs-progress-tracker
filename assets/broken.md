
<style>
  body {
    background-color: #ffffff;
    color: #0e0b2c; 
  }
</style>
# <h1 style="color:black;padding: 10px; display: inline-block;">Broken brute-force protection, IP block write-up</h1>

<img src="./img&codes/the login page for ip block.png">
IP is temporarily blocked if you submit 3 incorrect logins in a row. lets try the last time method injecting x-forward-for:...


<img src="./img&codes/x-forward-try.png">

It is blocked as before so we have to try another method :
1. If we login with our correct username and password the blocking count will be back to 0 this means: we can block being blocked by the server by login in to our account [weiter:peter] after every try of given password.
- i have created my own python code to alter every username.
  <a href="./img&codes/alteruser.py"> here for username</a> and <a href="./img&codes/usernames.txt"> here is altered user names</a>
- and for passwords <a href="./img&codes/alter.py"> and <a href="./img&codes/alteredlist.txt">here is the changed list of passwords</a>
<img src="./img&codes/usernamepayload.png">
so i have added them to burpsuite intruder by using **pitchfork attack**
<img src="./img&codes/passwordpayload.png">
both of them .and i have made some added this resource pool method to make one request at a time.
<img src="./img&codes/resource pool.png">
then started attacking 
<img src="./img&codes/start-attack.png">
At first there are 200 states codes for carlos but
there is one different states code (302) for this username 
<img src="./img&codes/passwordfound.png">
 ## <p style="color:red">Congratulation the lab is solved!</p>
<img src="./img&codes/labsolved.png">