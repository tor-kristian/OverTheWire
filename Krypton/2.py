cip = "OMQEMDUEQMEK"

alp = "abcdefghijklmnopqrstuvwxyz"

dicA = {}
dicB = {}

# Make dictionary of both (0:A), (1,B),...,(25:Z) and (A:0),(B:1),...,(Z:25)
for i in range(len(alp)):
    dicA[i] = alp[i]
    dicB[alp[i].upper()] = i

# Try every possible rotation of the ciphertext to find the correct plaintext
for i in range(len(alp)):
    k = ""
    for j in range(len(cip)):
        k+= dicA[(dicB[cip[j]]+i) % 26]

    # CAESARISEASY
    print(k.upper())

