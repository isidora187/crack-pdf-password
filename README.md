Python script for cracking password protected pdf files using brute-force method.
For each password in password file,it tries to open PDF using pikepdf.onen() with the current password.
If the password is correct it prints the time it takes to find the password and the password iteself.
The loop breaks once it finds the correct password.
