from class_multiple_choice import multiple_choice_test
import os


#%%
#if you want create empty fomrat to fill run:

#call and assign class:
Format=multiple_choice_test()

#produce an empty format to fill with question and choice
#arguments: number of question,number of choice

N_question=10
N_choice=4

Format.produce_format(N_question,N_choice)
#%%

#if you want produce test.TEX and test.PDF :

#call and assign class:
Test=multiple_choice_test()

#arguemnts: Number of test desired,path_format_filled,path_output_latex

N_test=10

working_directory=os.getcwd()

Path_filled_format=os.path.join(working_directory,"prova_filled")

Output_path=os.path.join(working_directory,"output_latex\\")

Path_original_answers=os.path.join(working_directory,"answers")
#execute 
Test.output(N_test,
            Path_filled_format,
            Output_path,
            Path_original_answers)






