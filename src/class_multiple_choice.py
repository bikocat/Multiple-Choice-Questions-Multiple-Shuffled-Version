from src.command.Template.utilities.empty_format import format_question
from shuffle_text import shuffle
import output_file
import numpy as np


class multiple_choice_test:

    def __init__(self):
        self.body_name = None

    def generate_template(self, n_quest, n_choices):

        print("\n\tBlank format created --->>> fill it!!!")
        format_question(n_quest, n_choices)

    def output(self, N_test, path_format, path_output, path_original_answers):
        Student_seed = np.arange(N_test)
        self.final_seed = ["final_test"+str(i) for i in Student_seed]
        total_output = [shuffle(int(i), path_format, path_original_answers)
                        for i in Student_seed]
        final_test = [i for i, j in total_output]
        answers_string = [j for i, j in total_output]
        output_file.latex_output(path_output, final_test, self.final_seed)

        with open(path_output + "Test_Correction.txt", "w+", encoding="utf-8") as doc:
            doc.write(output_file.txt_answers_output(
                path_original_answers, answers_string))

        print("\n \t --->>> Multiple Choice Test Created <<<---")
