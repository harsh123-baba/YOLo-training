
import os

'''
    helps to remove the classes.
'''
def read_text_file(file_name):
    f = open(f"{file_name}", "r")
    text = f.read()
    labels = text.splitlines()
    new_labels = "";
    for label in labels:

        if label[0] == "2":
            # need to remove this whole line
            print(label)
            continue;
        elif label[0] == "6":
            # need to remove this whole line
            print(label)
            continue;
        elif label[0] == "7":
            # need to remove this whole line
            print(label)
            continue;
        else:
            new_labels = new_labels + label + "\n"

    return new_labels
    
folder_path = r"F:\Harshit\Harshit_Testing\dateset_test\VisDrone\VisDrone2019-DET-test-dev\VisDrone2019-DET-test-dev\labels"
new_folder_path = r"F:\Harshit\Harshit_Testing\dateset_test\VisDrone\VisDrone2019-DET-test-dev\VisDrone2019-DET-test-dev\labels_1"
def main():
    # go to the file then extract info the create a new file the return true
    for (root,dirs,files) in os.walk(folder_path, topdown=True): 
        for file in files:
            content = read_text_file(folder_path+"/"+file)
            new_file_path = new_folder_path+"/"+file
            new_label_file = open(f"{new_file_path}", 'a+')
            new_label_file.write(content)
            new_label_file.close()
main()
# read_text_file('9999999_00877_d_0000402.txt')