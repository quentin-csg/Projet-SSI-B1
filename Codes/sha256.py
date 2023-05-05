import hashlib

# Hash to crack
hash_to_crack = "becf77f3ec82a43422b7712134d1860e3205c6ce778b08417a7389b43f2b4661" # this is the SHA-256 hash of the word "password"

# Read dictionary file
with open('./wordlists/password256.txt', "r") as file:
    for line in file:
        word = line.strip()
        # Hash the word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        # Compare the hash
        if hashed_word == hash_to_crack:
            print("Password found: " + word)
            break
    else:
        print("Password not found in dictionary.")