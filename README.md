# HIT137_Assignment_2

Hi alllllll

i think im gonna write a separate function to transform all the letters, instead of jam it all in encrypt_file. you guys can start on decrypt_file and verify_files if you want or i can do it later, i'm doing the encryption, so don't touch it. - Kevin

I just finished encryption, not sure if it's correct - Kevin

I just fixed your code, there's only 14 letters from "a" to "z", 12 letters from "o" - "z" and so on but you %26 for all instead of % on how many letters there are in the cycle. Also "o" - "z" start from ord ("o") not ord ("a") - Jade