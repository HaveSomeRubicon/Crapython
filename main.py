import ifuncs

crpy_path = "main.crpy"


def live_run_crpy(path):
    with open(path, 'r') as crpy_file:
        crpy_lines = crpy_file.readlines()
        crpy_lines = [line.replace("\n", "").split('.') for line in crpy_lines]
    print(crpy_lines)


live_run_crpy(crpy_path)
