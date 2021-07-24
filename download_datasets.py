import os 

def download_data(file_name=""):
    datasets_options = ['footprint_generation_separate','footprint_generation_combined']
    base_url = "https://raw.githubusercontent.com/banmala/fpgan-dataset/master/ROBIN/"
    ext = ".zip"
    source_file = base_url+file_name+ext
    zip_file = "datasets/"+file_name+ext

    TARGET_DIR = "datasets/"
    if not os.path.isdir(TARGET_DIR):
        os.mkdir(TARGET_DIR)


    os.system("wget -N "+source_file + " -O "+zip_file)
    os.system("unzip -q "+zip_file+" -d "+TARGET_DIR)

download_data("footprint_generation_combined")
