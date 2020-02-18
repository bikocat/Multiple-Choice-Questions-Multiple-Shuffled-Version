def format_question(n_questions,n_choices):
    
    string_choice=r'''\choice .....
        '''
    
    string_head_quest=r'''
    \question[points_quest] .....
	\begin{choices}
        '''
		
    string_end_quest=r'''
    \end{choices}
        '''
    
    choices_empty="".join(string_choice*n_choices)
    
    single_format_blank=string_head_quest+choices_empty+string_end_quest
    
    format_blank="".join(single_format_blank*n_questions)

    
    with open("format_to_fill.txt","w+",encoding="utf-8") as doc:
        doc.write(format_blank)
        
  