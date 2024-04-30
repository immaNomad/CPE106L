def navigate_file():
    filename = input("Enter a filename: ")
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file.readlines()]

    except FileNotFoundError: 
        print("File not found. Please try again.")
        return

    num_lines = len(lines)
    print(f"File has {num_lines} lines.")

    while True:
        line_num = int(input("Enter a line number (1-{}), or 0 to quit: ".format(num_lines)))
        if line_num == 0:
            break
        elif 1 <= line_num <= num_lines:
            print(lines[line_num - 1])
        else:
            print("Invalid line number. Please try again.")

navigate_file()
