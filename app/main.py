"""TODO"""
import os
import shutil

from gpt_code_comment import code_commentor


def process_python_files(
    source_folder: str, destination_folder: str,
):
    """TODO"""
    source_dir_path = os.path.realpath(source_folder)
    dest_dir_path = os.path.realpath(destination_folder)
    shutil.copytree(
        source_dir_path,
        dest_dir_path,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.git"),
    )
    # print(dest_dir_path)
    for root, dirs, files in os.walk(dest_dir_path):
        for folder in files:
            if folder.endswith(".py"):
                name = root + "/" + str(folder)
                with open(name, "r", encoding="utf-8") as f:
                    code = f.read()
                if code == "":
                    continue
                try:
                    code_extracted = code_commentor(code)
                except Exception as e:
                    print(f"Could not process {name}, {e}")

                else:
                    if code_extracted != 0:
                        with open(name, "w", encoding="utf-8") as f:
                            f.write(code_extracted.commented_code)
                        print(name)
                        print(code_extracted.notes)
                        print("-----------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    src_file_path = input("Enter code directory to be commented: ")
    dest_file_path = input(
        "Where do you want the commented code directory to be? please give the path of the root folder: "
    )
    process_python_files(src_file_path, dest_file_path)
