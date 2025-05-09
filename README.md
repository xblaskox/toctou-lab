# toctou-lab
A safe, contained, and punchy demo of a TOCTOU (Time of Check to Time of Use) race condition using Python, right on your own system — no root access, no risk, just raw clarity.

Steps: copy the files "victim.py" and "attacker.py" to a new directory. I used /pwned/ because of course I did.
Ignore the evil_payload and demo_file as you can create these on your own by running this:
echo "This is safe content." > /tmp/demo_file.txt
echo ":dragon: This is the malicious payload :dragon:" > /tmp/evil_payload.txt
The micdrop file is just something I wrote up to "cat" after the lab demo has been run as an explanation of what occurred.
Enjoy and have fun learning.
