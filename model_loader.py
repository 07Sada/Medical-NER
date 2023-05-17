import zipfile
import spacy
import os

# name of the zip file
zip_file_name = "model-best.zip"

# current working directory
current_directory = os.getcwd()


# check if the extracted version of the zip file exists
def extracter(current_directory=current_directory, zip_file_name=zip_file_name):
    if not os.path.isdir(os.path.join(current_directory, zip_file_name.replace(".zip", ""))):
    # Extract the zip file
        with zipfile.ZipFile(zip_file_name, "r") as zip_file:
            zip_file.extractall(current_directory)
        nlp = spacy.load("model-best")
    else:
        nlp = spacy.load("model-best")
    return nlp

nlp = extracter(current_directory=current_directory, zip_file_name=zip_file_name)