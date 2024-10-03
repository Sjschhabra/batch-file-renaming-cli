import os

while True:
    x = input("\n\033[1;31m1. Enter file format you want to work with (enter ._filetype_):\033[0m")
    while True:
        
        project_directory = os.path.dirname(os.path.abspath(__file__))
        txt_files = [f for f in os.listdir(project_directory) if f.endswith(x)]
        print(f"\nFiles Present in the directory are: {txt_files}")
        z = input(f"\033[1;31m2. Enter prefix you want for all the \"{x}\" files(or b:back to 1st step):\033[0m")
        if z!="b":
            pass
        else:
            print("Going back to the 1st step")
            break
        # Get all files with the specified prefix
        prefix_files = [file for file in txt_files if file.startswith(z)]

        # Rename files with the specified prefix to have the prefix and sequential numbers
        if prefix_files:
            i = 1
            for file in prefix_files:
                new_name = f"dbagHdrrtns-{i}{x}"
                os.rename(os.path.join(project_directory, file), os.path.join(project_directory, new_name))
                i += 1
        txt_files2 = [f for f in os.listdir(project_directory) if f.endswith(x)]
        print(f"\n(Ignore this print- {txt_files2})")
        # Then, rename the remaining files sequentially
        i = 1
        q=input("\033[1;31m3. Would you like to change file format (enter file format or press enter to skip):\033[0m")
        if q!="":
            x=q
        else:
            pass
    
        for file in txt_files2:
                new_name = f"{z}-{i}{x}"
                os.rename(os.path.join(project_directory, file), os.path.join(project_directory, new_name))
                i += 1

        print("\n\n\033[1;95m----Task Completed----\033[0m\n\n\n")
