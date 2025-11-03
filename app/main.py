

def copy_file(command: str) -> None:
    list_of_command = command.split()
    if len(list_of_command) < 3:
        return
    file_to_copy = list_of_command[1]
    copied_file = list_of_command[2]
    if command != str(f"cp {file_to_copy} {copied_file}"):
        return
    if file_to_copy == copied_file:
        return
    try:
        open(file_to_copy)
    except FileNotFoundError:
        return
    with (open(file_to_copy, "r") as file_in,
          open(copied_file, "w") as file_out):
        for line in file_in.readlines():
            file_out.write(line)
