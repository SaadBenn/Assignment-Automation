# os for file management
import os

from submit_assignment import submit_assignment


def find_assignment():
    submission_dir = '/Users/saad/desktop/Completed_Assignments'

    # grab the classes folder
    directory_list = list(os.listdir(submission_dir))

    for directory in directory_list:
        # grab the assignments inside each classes
        file_list = list(os.listdir(os.path.join(submission_dir, directory)))

        # check if there's any files in the directory
        if len(file_list) != 0:
            # Build tuple of (folder, file) to turn in
            file_tup = (directory, file_list[0])

    if len(file_tup) == 0:
        print('No files to submit')

    else:
        print('Assignment "{}" for "{}" found.'.format(file_tup[1], file_tup[0]))
        input('Press enter to proceed: ')
        submit_assignment(file_tup)
