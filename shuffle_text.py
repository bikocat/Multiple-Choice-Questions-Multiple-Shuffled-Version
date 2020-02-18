import numpy as np
import random
from material import header_end
from material import body_of_text
from material import answers_right
import string


#%%


def shuffle(n,path_format,path_answers_right):
    
    
    
    prova=body_of_text(path_format)
   
    
    header=header_end()[0]
    end=header_end()[1]
    
    P=prova.replace("\t","")
    
    prova_list=P.splitlines()
    while("" in prova_list) : 
        prova_list.remove("") 
    
    
    
    index_question=[]
    
    for i in prova_list :
        
        if "\question" in i:
            
            idx_q=prova_list.index(i)
            index_question.append(idx_q)
            
            
    index_choice=[]
    
    for i in range(len(prova_list)) :
        
        if "\choice" in prova_list[i]:
            
            index_choice.append(i)
        
        
    index_beg_choice=[]
    index_end_choice=[]
    
    for i in range(len(prova_list)) :
        
        if r"\begin{choices}" == prova_list[i]:
            
            
            index_beg_choice.append(i)
            
        elif  r"\end{choices}" == prova_list[i]:
            
            
            index_end_choice.append(i)
            
            
    prova_idx=np.arange(len(prova_list))
    Ar=np.split(prova_idx,index_question)
    
    i=0
    clean_ar=[]
    
    for i in range(len(Ar)):
        
        clean=set(index_choice).intersection(Ar[i])
        clean=list(clean)
        clean.sort(reverse = False)
        clean_ar.append(list(clean))
        
    #remove empty element
    clean_ar = [x for x in clean_ar if x != []]
    
    #shuffle choices no question
    random.seed(n)
    clean_ar_shuffle_choices_1=[random.sample(list(i),len(i)) for i in clean_ar]
    
    #insert \begin choices first elemetn of sublist
    
    clean_ar_shuffle_env_choices=np.concatenate((np.array([index_beg_choice]).T,clean_ar_shuffle_choices_1),1)
    
    #insert \end choices last element of sublist
    
    clean_ar_shuffle_env_choices=np.concatenate((clean_ar_shuffle_env_choices,np.array([index_end_choice]).T),1)    
    
    #insert index question first element sublist
    
    clean_ar_shuffle_choices=np.concatenate((np.array([index_question]).T,clean_ar_shuffle_env_choices),1) 
      
    #shuffle question 
    random.seed(n)    
    clean_ar_shuffle_question=random.sample(list(clean_ar_shuffle_choices),len(clean_ar_shuffle_choices))  
    
    #flat array     
    
    final_idx_flat=[i for l in clean_ar_shuffle_question for i in l ]
    
    #get element from shuffled index
    
    test_shuffled=[prova_list[i] for i in final_idx_flat]
    

    final_test=header+("\n".join(test_shuffled))+"\n"+end
    
   
    
    #answers file
    
    answers=answers_right(path_answers_right)
    
    alphabet=string.ascii_uppercase
    
    n_choice=int(len(index_choice)/len(index_question))
    
    #letter_format
    standard_letters=[[alphabet[i] for i in range(n_choice)] for j in range(len(index_question))]
    
    #shuffle choice
    random.seed(n)
    quest_letters_shuffle_choice=[random.sample(i,len(i))  for i in standard_letters]
    
    #shuffle question
    random.seed(n)
    quest_letters_shuffle_question=random.sample(quest_letters_shuffle_choice,len(index_question))
    
    
    #shuffle right answers to retrieve his position
    random.seed(n)
    right_ans_quest=random.sample(answers,len(index_question))
    
    #index right answer
    right_answer_shuffled_number=[quest_letters_shuffle_question[i].index(right_ans_quest[i]) for i in range(len(index_question))]
    
    #replace choice to real letter in latex
    right_answer=[alphabet[i] for i in right_answer_shuffled_number]
    
    shuffled_answers=str(n)+"_TEST: " + ",".join(right_answer)
    
    return(final_test,shuffled_answers) #multiple choice
    
    
#%%


def answers_shuffle(n,path_answers_right) :
    
    answers=answers_right(path_answers_right)
    random.seed(n)
    shuffled_answers=random.sample(answers,len(answers))
    
    shuffled_answers=str(n)+"_TEST: " + ",".join(shuffled_answers)
    
    return(shuffled_answers)
    
