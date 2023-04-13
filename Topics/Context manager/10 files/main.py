n_files = 10
files = []

for n in range(1, n_files + 1):
    with open('file' + str(n) + '.txt', 'w') as f:
        f.write(str(n))