import  os,subprocess
from shuffle_text import answers_shuffle
    
#%%

def latex_output(path,final_test,final_seed):

    
    j=0
    for i in final_test:
        
        complete_path=os.path.join(path+final_seed[j] +'.tex')
        
        with open(complete_path,"w+",encoding="utf-8") as doc:
            doc.write(i)
        
        commandLine = subprocess.Popen(['pdflatex',final_seed[j]+".tex"],
                                       cwd=path)
        commandLine.communicate()
        commandLine.kill()
        
        os.unlink(path+final_seed[j] +'.aux')
        os.unlink(path+final_seed[j] +'.log')
        
        j+=1
        
#%%
        
def txt_answers_output(path_answers_right,answers):
    
        list_ans_n_test="\n".join(answers)
        
        
        return(list_ans_n_test)
          
    
