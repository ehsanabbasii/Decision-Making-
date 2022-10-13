# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:29:17 2022

@author:Ehsan Abbasi
"""

# This code demonstrates the sensivity analyse of the Job offer package optimazation in a two-sided matching


import pandas as pd 
from mip import *


def clean_utilityp(utilityP_list):
    clean_utility_list =[]
    for i in range(0,len(utilityP_list)):
        
        clean_utility_temp=[]
        for j in range(0,len(utilityP_list[0])):
            ut= xsum(utilityP_list[i][j]).x
            clean_utility_temp.append(ut)
            
        clean_utility_list.append(clean_utility_temp) 
        
    return clean_utility_list

    
class Person :

    
    
    def __init__(self ,name ,education , english,general_skill,experince,pshyco_test,person_weight_list):
        self.name =name
        self.education =education
        self.english =english
        self.general_skill =general_skill
        self.experince =experince
        self.pshyco_test =pshyco_test
        self.person_weight_list =person_weight_list
        
        self.edu=edu_dict[education]
        self.lan=lan_dict[english]
        self.gen=gen_dict[general_skill]
        self.exp=exp_dict[experince]
        self.psy=psy_dict[pshyco_test]


edu_dict= {"None":1,"Diploma":2,"BSC":4,"MSC":6,"PHD":8}
lan_dict= {"low":1,"medium":2,"good":3,"advanced":4,"native":5}
gen_dict={"low":1,"medium":2,"good":4,"high":8,"advanced":10}
exp_dict={"0-5":1,"5-10":2,"10-15":4,"15-20":6,"20 and more":8}
psy_dict = {"low":1,"medium":2,"good":4,"high":8,"excellent":10}
            
#declaring persons
# order is name ,education , english,general_skill,experince,pshyco_test
pr0 =Person("Paul" , "MSC", "native" , "good" , "0-5" , "good",[0.5,0.2,0.2,0.1])
pr1 =Person("Yahn" , "PHD", "medium" , "medium" , "10-15" , "low",[0.4,0.2,0.15,0.25])
pr2 =Person("Siraj" , "BSC", "good" , "high" , "0-5" , "medium",[0.35,0.1,0.25,0.3])
pr3 =Person("Saeed" , "PHD", "advanced" , "advanced" , "15-20" , "excellent",[0.6,0,0.3,0.1])
pr4 =Person("Alex" , "BSC", "advanced" , "high" , "0-5" , "good",[0.5,0.2,0.15,0.15])
pr5 =Person("Dimitry" , "MSC", "low" , "low" , "20 and more" , "high",[0.55,0.15,0.15,0.15])
pr6 =Person("David" , "MSC", "advanced" , "advanced" , "10-15" , "excellent",[0.3,0.6,0.1,0])        

organs_dict = {
'Organ A' : [0.4,0.1,0.1,0.25,0.15],
'Organ B' : [0.36,0.04,0.2,0.3,0.1],
'Organ C' : [0.31,0.14,0.16,0.14,0.25]

              }
persons_dict = {
'Candidate 1'   :      [0.5,0.2,0.2,0.1]     ,
'Candidate 2'   :      [0.4,0.2,0.15,0.25],
'Candidate 3'   :      [0.35,0.1,0.25,0.3],
'Candidate 4'   :      [0.6,0,0.3,0.1],

'Candidate 5'    :      [0.5,0.2,0.15,0.15],
'Candidate 6'    :      [0.55,0.15,0.15,0.15],    
'Candidate 7'    :      [0.3,0.6,0.1,0],
                }
organ_index_dict ={
    0 : "A",
    1 : "B",
    2: "C"
}

candidate_index_dict ={
    0 : "1",
    1 : "2",
    2 : "3",
    3 : "4",
    4 : "5",
    5 : "6",
    6 : "7",
}

or_df = pd.DataFrame(organs_dict)
or_df =or_df.T
or_columns=["education" , "english","general_skill","experince","pshyco_test"]
or_df.columns=or_columns
or_df

pr_df = pd.DataFrame(persons_dict)

weigh_or_list = ["Organ A","Organ B","Organ C"]
persons_list= [pr0,pr1,pr2,pr3,pr4,pr5,pr6]

utility_list = []
utility_dict ={}
for i in weigh_or_list:
    U_list=[]
    for j in persons_list:
        
        U = organs_dict[i][0] * j.edu +organs_dict[i][1] * j.lan+organs_dict[i][2] * j.gen +organs_dict[i][3] * j.exp+organs_dict[i][4] * j.psy
        U_list.append(U)
        
        print ( "Utility for {:} with {:} is {:0.5} ".format(i,j.name,U))
    utility_list.append(U_list)
    utility_dict[i] = U_list 


pr_df =pr_df.T
pr_columns=["sallary","bonus","flexibility","remote"]
pr_df.columns=pr_columns
pr_df.to_excel("person_weight.xlsx")

ut_df = pd.DataFrame(utility_dict)
ut_df.index = ['Candidate 1','Candidate 2','Candidate 3','Candidate 4','Candidate 5','Candidate 6','Candidate 7']

person_weight_list =[
    [0.5,0.2,0.2,0.1]     ,
[0.4,0.2,0.15,0.8],
[0.35,0.1,0.25,0.3],
[0.5,0.1,0.1,0.3],
[0.55,0.15,0.15,0.15],

[0.5,0.2,0.15,0.15],
[0.3,0.6,0.1,0],
]

###########################################################################
##### #######################################################################
##### ######################################################################
##### ########################################################################
##### ########################################################################
#####     ####################################################################
##############################################################################


scenario_seed_list=[
    
    
    [100 , 7 , 1 , 0.1 , (1/100)*176 * 7 , (1/100)*176 * 7],
    [50 , 7 , 1 , 0.1 , (1/100)*176 * 7 , (1/100)*176 * 7],
    [50 , 7 , 1 , 0.1,(1/100)*176 * 7 , (1/100)*176 * 7],
    [50 , 7 , 1, 0.1, (1/100)*176 * 7 , (1/100)*176 * 7],
    [50 , 7 , 1 , 1 , (1/100)*176 * 7 , (1/100)*176 * 7],
    [50 , 7 , 1 , 1 , (5/100)*176 * 7 , (10/100)*176 * 7],
    [20 , 7 , 1 , 1 , (5/100)*176 * 7 , (10/100)*176 * 7],
    [5 , 7 , 1 , 0.1 , (10/100)*176 * 7 , (20/100)*176 * 7],
    [5 , 7 , 1 , 0.1 , (1/100)*176 * 7 , (2/100)*176 * 7],
    
    
    
    
    ]








for seed in scenario_seed_list:    
    print(seed[0])
    model = Model()
    model.emphasis=2
    
    n_person = 5 # Max 7
    n_organ = 3  # Max 3
    # It is proved that maximum number is multiplition of the number of organs and persons.
    n_time_step= n_organ * n_person +1 
    
    M= 1 * 10 **9
    
    #Organ's job offer packages are the decision variable, that are stored in a 2D list called D_list
    D_list = []
    
    # Each item retains upper bounds and lower bound
    D_item_upper_bounds = [
                    [25,5,4,1] # organ A  (sallary,bonus,flexibility,remote)
                     ,[9,4,2,0]
                     ,[8,5,1,1]]
    
    D_item_lower_bounds = [
                    [5,0,0,0] # organ A 
                     ,[9,4,2,0]# organ B
                     ,[8,5,1,1]]# organ C
    
    n_package_items= 4
    # In this example, number of job offer package's items is 4 which points to sallary and reward.
    for i in range(0,n_organ):
        D_list_temp =[]
        for p in range(0,n_package_items):
            if p <2 :
                D_list_temp.append(model.add_var(name = "d{:}{:}".format(i,p),lb=D_item_lower_bounds[i][p],ub= D_item_upper_bounds[i][p]))
            #Since the essneses of item 3 and 4 are diffrenet
            #Flexiblilty
            elif p==2:
                D_list_temp.append(model.add_var(name = "d{:}{:}".format(i,p),var_type=INTEGER,lb=D_item_lower_bounds[i][p],ub= D_item_upper_bounds[i][p]))
            #remotablity
            elif p==3:
                D_list_temp.append(model.add_var(name = "d{:}{:}".format(i,p),var_type=BINARY,lb=D_item_lower_bounds[i][p],ub= D_item_upper_bounds[i][p]))
        D_list.append(D_list_temp)
    
    CH_list = []
    for i in range(0,n_organ):
        ch_temp=[]
        for j in range(0,n_person):
            ch_temp_temp=[]
            for k in range(0,n_time_step):
                if k ==0:
                    ch_temp_temp.append(model.add_var(name = "ch{:}{:}{:}".format(i,j,k) , var_type=BINARY,lb=0,ub =0 ))
                else :
                    ch_temp_temp.append(model.add_var(name = "ch{:}{:}{:}".format(i,j,k) , var_type=BINARY))
            ch_temp.append(ch_temp_temp)
            
        CH_list.append(ch_temp)
    
    # CHP_list points to candidate's choosing organs.
    
    CHP_list = []
    for i in range(0,n_organ):
        chp_temp=[]
        for j in range(0,n_person):
            chp_temp_temp=[]
            for k in range(0,n_time_step):
                if k ==0:
                    chp_temp_temp.append(model.add_var(name = "chp{:}{:}{:}".format(i,j,k) , var_type=BINARY,lb=0,ub =0))
                else :              
                    chp_temp_temp.append(model.add_var(name = "chp{:}{:}{:}".format(i,j,k) , var_type=BINARY))
        
            chp_temp.append(chp_temp_temp)
            
        CHP_list.append(chp_temp)    
    
        
        
      
        
        
    IN_list = []
    for i in range(0,n_organ):
        in_temp=[]
        for j in range(0,n_person):
            in_temp_temp=[]
            for k in range(0,n_time_step):
                if k ==0:
                    in_temp_temp.append(model.add_var(name = "interview{:}{:}{:}".format(i,j,k),var_type=BINARY,ub=0))
                else:
                    
                    in_temp_temp.append(model.add_var(name = "interview{:}{:}{:}".format(i,j,k),var_type=BINARY))
        
            in_temp.append(in_temp_temp)
            
        IN_list.append(in_temp)        
        
        
        
    
    ZITA_list=[] 
    for i in range(0,n_organ):
        zita_temp=[]
        for j in range(0,n_person):
            zita_temp_temp=[]
            for k in range(0,n_time_step):
                zita_temp_temp.append(model.add_var(name = "zita{:}{:}{:}".format(i,j,k) , var_type=BINARY))
             
            zita_temp.append(zita_temp_temp)
            
        ZITA_list.append(zita_temp)  
    
    
    OPTION_list=[] 
    for i in range(0,n_organ):
        OPTION_temp=[]
        for j in range(0,n_person):
            OPTION_temp_temp=[]
            for k in range(0,n_time_step):
                OPTION_temp_temp.append(model.add_var(name = "OPTION{:}{:}{:}".format(i,j,k)))
        
            OPTION_temp.append(OPTION_temp_temp)
            
        OPTION_list.append(OPTION_temp) 
        
    OPTION_0_list=[] 
    for i in range(0,n_organ):
        OPTION_0_temp=[]
        for j in range(0,n_person):
            OPTION_0_temp_temp=[]
            for k in range(0,n_time_step):
                OPTION_0_temp_temp.append(model.add_var(name = "OPTION_0{:}{:}{:}".format(i,j,k)))
        
            OPTION_0_temp.append(OPTION_0_temp_temp)
            
        OPTION_0_list.append(OPTION_0_temp)    
        
    OPTION_1_list=[] 
    for i in range(0,n_organ):
        OPTION_1_temp=[]
        for j in range(0,n_person):
            OPTION_1_temp_temp=[]
            for k in range(0,n_time_step):
                OPTION_1_temp_temp.append(model.add_var(name = "OPTION_1{:}{:}{:}".format(i,j,k)))
        
            OPTION_1_temp.append(OPTION_1_temp_temp)
            
        OPTION_1_list.append(OPTION_1_temp)
        
    OPTION_2_list=[] 
    for i in range(0,n_organ):
        OPTION_2_temp=[]
        for j in range(0,n_person):
            OPTION_2_temp_temp=[]
            for k in range(0,n_time_step):
                OPTION_2_temp_temp.append(model.add_var(name = "OPTION_2{:}{:}{:}".format(i,j,k)))
        
            OPTION_2_temp.append(OPTION_2_temp_temp)
            
        OPTION_2_list.append(OPTION_2_temp)
            
    OPTION_3_list=[] 
    for i in range(0,n_organ):
        OPTION_3_temp=[]
        for j in range(0,n_person):
            OPTION_3_temp_temp=[]
            for k in range(0,n_time_step):
                OPTION_3_temp_temp.append(model.add_var(name = "OPTION_3{:}{:}{:}".format(i,j,k)))
        
            OPTION_3_temp.append(OPTION_3_temp_temp)
            
        OPTION_3_list.append(OPTION_3_temp)
            
    
    all_options = [OPTION_0_list,OPTION_1_list,OPTION_2_list,OPTION_3_list]     
    
    
    GAMA_list = []
    for i in range(0,n_organ):
        gama_temp=[]
        for j in range(0,n_person):
            gama_temp_temp=[]
            for k in range(0,n_time_step):
                
                gama_temp_temp.append(model.add_var(name = "gama{:}{:}{:}".format(i,j,k)))
        
            gama_temp.append(gama_temp_temp)
            
        GAMA_list.append(gama_temp)  
        
        
        
    GAMA_0_list = []
    for i in range(0,n_organ):
        gama_0_temp=[]
        for j in range(0,n_person):
            gama_0_temp_temp=[]
            for k in range(0,n_time_step):
                
                gama_0_temp_temp.append(model.add_var(name = "gama0{:}{:}{:}".format(i,j,k)))
        
            gama_0_temp.append(gama_0_temp_temp)
            
        GAMA_0_list.append(gama_0_temp)  
        
    
    
        
    GAMA_1_list = []
    for i in range(0,n_organ):
        gama_1_temp=[]
        for j in range(0,n_person):
            gama_1_temp_temp=[]
            for k in range(0,n_time_step):
                
                gama_1_temp_temp.append(model.add_var(name = "gama1{:}{:}{:}".format(i,j,k)))
        
            gama_1_temp.append(gama_1_temp_temp)
            
        GAMA_1_list.append(gama_1_temp)      
    
        
    GAMA_2_list = []
    for i in range(0,n_organ):
        gama_2_temp=[]
        for j in range(0,n_person):
            gama_2_temp_temp=[]
            for k in range(0,n_time_step):
                
                gama_2_temp_temp.append(model.add_var(name = "gama2{:}{:}{:}".format(i,j,k)))
        
            gama_2_temp.append(gama_2_temp_temp)
            
        GAMA_2_list.append(gama_2_temp)  
        
    
    
        
    GAMA_3_list = []
    for i in range(0,n_organ):
        gama_3_temp=[]
        for j in range(0,n_person):
            gama_3_temp_temp=[]
            for k in range(0,n_time_step):
                
                gama_3_temp_temp.append(model.add_var(name = "gama3{:}{:}{:}".format(i,j,k)))
        
            gama_3_temp.append(gama_3_temp_temp)
            
        GAMA_3_list.append(gama_3_temp)      
            
        
    all_gamas = [GAMA_0_list,GAMA_1_list,GAMA_2_list,GAMA_3_list]     
    
    
    ALPHA_list = []
    for i in range(0,n_organ):
        ALPHA_list_temp =[]
        for t in range(0,n_time_step):
            if t==0 :
                
                ALPHA_list_temp.append(model.add_var(name = "alpha{:}{:}".format(i,t),lb=0 , ub=0))
            else :
                
                ALPHA_list_temp.append(model.add_var(name = "alpha{:}{:}".format(i,t)))
        
                                   
        ALPHA_list.append(ALPHA_list_temp)    
        
    ALPHA_P_list = []
    for j in range(0,n_person):
        ALPHA_P_list_temp =[]
        for t in range(0,n_time_step):
            if t==0 :
                ALPHA_P_list_temp.append(model.add_var(name = "alphaP{:}{:}".format(j,t),lb=0,ub=0)) 
            else :    
                ALPHA_P_list_temp.append(model.add_var(name = "alphaP{:}{:}".format(j,t)))
        
                                   
        ALPHA_P_list.append(ALPHA_P_list_temp)      
        
    utilityP_list =[]
    
    # Utility of organs in side of candidate's view are decision varibles of the model.
    # And stored in a 2D list.
    
    for i in range(0,n_organ):  
        Up_list = []
        for j in range(0,n_person):     
            Up_0 = person_weight_list[j][0]*D_list[i][0]
            Up_1 = person_weight_list[j][1]*D_list[i][1]
            Up_2 = person_weight_list[j][2]*D_list[i][2]
            Up_3 = person_weight_list[j][3]*D_list[i][3]
            
            Up_list.append([Up_0,Up_1,Up_2,Up_3])
            
        utilityP_list.append(Up_list)   
    #linearization for constraint 2
    # Gama is a subsidiary variable
    
    # We have to linarize the following constraints:  
    for i in range(0,n_organ):   
        
        for j in range(0,n_person):  
        
            for t in range(0,n_time_step): 
                
                for p in range(0,n_package_items):
    
                    model +=  all_gamas[p][i][j][t] <= utilityP_list[i][j][p]  ,"Gama line"
                    model +=  all_gamas[p][i][j][t] <= D_item_upper_bounds[i][p] * CHP_list[i][j][t] ,"Gama line"
                    model +=  all_gamas[p][i][j][t] >= utilityP_list[i][j][p] + D_item_upper_bounds[i][p] *(CHP_list[i][j][t]-1) ,"Gama line"
                    model +=  all_gamas[p][i][j][t] >= 0 ,"Gama line"
    
                
                
                
                
                
              
            
            
            
            
                GAMA_list[i][j][t] = GAMA_0_list[i][j][t] + GAMA_1_list[i][j][t] + GAMA_2_list[i][j][t]+GAMA_3_list[i][j][t]
                
                
                    
    
    for i in range(0,n_organ):   
        
        for j in range(0,n_person):                          
            
            for t in range(1,n_time_step): 
                
                model += ZITA_list[i][j][t] == (1 - xsum(IN_list[i][j][k] for k in range(t ) ) + CH_list[i][j][t-1])
                
                ####  ZITAij can NOT be multipled by U'ij since it creats non-linearity term. We have to make it linearized
                
                for p in range(0,n_package_items):
                
                
                    model +=  all_options[p][i][j][t] <= utilityP_list[i][j][p] ,"OPTIon"
                    model +=  all_options[p][i][j][t] <= D_item_upper_bounds[i][p] * ZITA_list[i][j][t],"OPTIon"
                    model +=  all_options[p][i][j][t] >= utilityP_list[i][j][p] + D_item_upper_bounds[i][p] *(ZITA_list[i][j][t]-1),"OPTIon"
                    model +=  all_options[p][i][j][t] >= 0
    
                
                
                
                
                
                OPTION_list[i][j][t] = OPTION_0_list[i][j][t] + OPTION_1_list[i][j][t] + OPTION_2_list[i][j][t] + OPTION_3_list[i][j][t]
                                     
                model += ALPHA_P_list[j][t] >= OPTION_list[i][j][t] , "Alpha' is the max"
          #      model += ALPHA_P_list[j][t] <= OPTION_list[i][j][t] + M * (1 - CHP_list[i][j][t])
                
                
                #########NEW constraint
                model += CH_list[i][j][t] <= CHP_list[i][j][t]    
    
    # constraint 7 ::  needing some linerazition .. 
    
    for i in range(0,n_organ):   
        for j in range(0,n_person):          
            for t in range(0,n_time_step):                     
                X = xsum(CHP_list[i][j][k] for k in range(0,t+1))
                ###############################################
                #### LINEARIZATION  SNIPPET #################3
                x0=model.add_var(name = "x0_{:}{:}{:}".format(i,j,t),lb=0,var_type=INTEGER)
                x1=model.add_var(name = "x1_{:}{:}{:}".format(i,j,t),lb=0,var_type=INTEGER)
                x2 =model.add_var(name = "x2_{:}{:}{:}".format(i,j,t),lb=0,var_type=INTEGER)
                t0=model.add_var(name = "t0_{:}{:}{:}".format(i,j,t),var_type=BINARY)
                t1=model.add_var(name = "t1_{:}{:}{:}".format(i,j,t),var_type=BINARY)
                t2=model.add_var(name = "t2_{:}{:}{:}".format(i,j,t),var_type=BINARY)
                model += x0 <= 0.001*t0   ,"Interview line"
                model += (0.002)*t1 <= x1 ,"Interview line"
                model += 1*t1 >= x1 ,"Interview line"
                model += (1.001)*t2 <= x2,"Interview line"
                model += x2 <= (n_time_step)*t2,"Interview line"
                model += x0+x1+x2 ==X,"Interview line"
                model += t0 +t1 +t2 ==1 ,"Interview line"
                ###############################################
                IN_list[i][j][t] =0 * x0 + 0*x1 +  0*x2 + 0*t0 + 1*t1 + 0*t2
                
    #constraint 8
    for i in range(0,n_organ):         
        model += xsum(CH_list[i][j][n_time_step-1] for j in range(0,n_person) ) ==1
        for j in range(0,n_person):
            model += xsum(IN_list[i][j][t] for t in range(n_time_step) ) <=1 ,"constraint"
                        
                
    for j in range(0,n_person):
        for t in range(1,n_time_step):#was set to 0  
            # CONSTRAINT 2
            model += ALPHA_P_list[j][t] == xsum(GAMA_list[i][j][t] for i in range(0,n_organ))," CONSTRAINT 2"
              
             # cosnstraint 3  in each time step T, person can choose at most 1 organ
            
            model += xsum(CHP_list[i][j][t] for i in range(0,n_organ)) <= 1.0001     
            
    # Constraint 4 :
    for i in range(0,n_organ):   
        
        for j in range(0,n_person):                          
            
            for t in range(1,n_time_step): 
                
                 model += ALPHA_list[i][t] >= CHP_list[i][j][t] * utility_list[i][j]  ,"alpha * utilt"                   
    # Constraint 5 :
    for i in range(0,n_organ):
        for t in range(0,n_time_step):
            
            model += ALPHA_list[i][t] == xsum(CH_list[i][j][t] * utility_list[i][j] for j in range(0,n_person)) , "alpha is the max"
            
            # Cosnstraint 6 : in each time step T, an organ can accept at most 1 resume from 1 person        
            model += xsum(CH_list[i][j][t] for j in range(0,n_person)) <=1   ,"1 person at time"
                
    
    
   
    
    Uj_A=ALPHA_list[0][n_time_step-1]
    
    # In the last time step, the personnel selection is done.
    rev_0 = seed[0]
    ave_salary = seed[1]
    expected_cost_item_0 = seed[2]
    expected_cost_item_1 = seed[3]
    expected_cost_item_2 = seed[4]
    expected_cost_item_3 = seed[5]
    
    model.objective = minimize(expected_cost_item_0 *D_list[0][0] + expected_cost_item_1*D_list[0][1] + expected_cost_item_2*D_list[0][2] + expected_cost_item_3*D_list[0][3] -rev_0 * Uj_A  )                
    model.optimize()    
    print("The optimum job offer package for Organ A is to offer\n {:} as a salary \n {:} as a reward \n {:} hours as the flexibility time and \n {:} as remote to recruite a suitable candidate ".format(D_list[0][0].x,D_list[0][1].x,D_list[0][2].x,D_list[0][3].x))   
    total_cost = expected_cost_item_0 *D_list[0][0] + expected_cost_item_1*D_list[0][1] + expected_cost_item_2*D_list[0][2] + expected_cost_item_3*D_list[0][3]
    print("the total cost is :",total_cost.x) 
    print(clean_utilityp(utilityP_list))
    
    for i in range(0,n_organ):
        for j in range(0,n_person):
            if CHP_list[i][j][n_time_step-1].x == CH_list[i][j][n_time_step-1].x ==1:
                print("Organ {:} and Candidate {:} are a stable match".format(organ_index_dict[i],candidate_index_dict[j])) 
    
    
    