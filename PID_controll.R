#### PID check: 

## Read file:

#help(read.csv)
pid_csv = read.csv()

library(xlsx) #https://cran.r-project.org/web/packages/xlsx/xlsx.pdf
pid_xlsx = read.xlsx()

PIDs = ###SET THIS EQUAL TO PID vector###

  
pid_control = function(p_vector){
  
  ##Constant verification vectors: http://www.fnrinfo.no/Teknisk/KontrollsifferSjekk.aspx
  control_1_10_vector = c(3,7,6,1,8,9,4,5,2,1)
  
  control_2_11_vector = c(5,4,3,2,7,6,5,4,3,2,1)
  
  #Booleans:
  bool1 = FALSE
  bool2 = FALSE
  
  #Assuming vector:
  n = length(p_vector)
  
  #Initialise return:
  results_matrix = matrix(0,nrow = n,ncol = 3)
  
  #Check string assumption:
  check_string = all(is.character(p_vector))
  if(!check_string){
    print("Not all PIDs are strings..? Converting along the processing.")
  }
  else{
    print("All PIDs are strings...")
  }
  
  #Correct for length with 0 and split confirm assumption:
  for(i in 1:n){
    #Getting i'th one.
    this_pid = p_vector[i]
    
    #Ensuring string:
    this_pid = as.character(this_pid)
    
    #Splitting retrieved pid and converting to integers for later calculations:
    split_pid = as.numeric(strsplit(this_pid,split = "")[[1]])
    ith_length = length(split_pid)
    
    #Trouble checking:
    is_corrected =  0
    if(ith_length != 11){
      #Add zeroes at the beginning of the vector; though supposedly not possible with more than 1 zero at the beginning:
      is_corrected =  1
      zero_v = rep(0,ith_length)
      split_pid = c(zero_v,split_pid)
    }
    if(ith_length < 10){
      warning("Length of PID is less than 10..!")
      print(this_pid)
    }
    if(ith_length > 11){
      warning("Length of PID is larger than 11..!")
      print(this_pid)
    }
    
    
    #Control 1:
    extracted_10 = split_pid[c(1:10)]
    vector_prod_10 = extracted_10 * control_1_10_vector
    modulus_11_10 = sum(vector_prod_10) %% 11
    
    #Control 2:
    vector_prod_11 = split_pid * control_2_11_vector
    modulus_11_11 = sum(vector_prod_11) %% 11
    
    #Changing accordingly:
    if(modulus_11_10 == 0){
      bool1 = TRUE
    }
    if(modulus_11_11 == 0){
      bool2 = TRUE
    }
    
    #Storing result:
    this_pid_conlusion = bool1*bool2
    
    results_matrix[i,1] = i
    results_matrix[i,2] = this_pid_conlusion
    results_matrix[i,3] = is_corrected
  }
  
  #Returning result:
  colnames(results_matrix) <- c("Nr","OK","Corrected")
  
  results_matrix = as.data.frame(results_matrix)
  results_matrix$PID = p_vector
  
  return(results_matrix)
}
  





### Testing area: (Seems to work ok)

test_string = "12354123456"

strsplit(test_string,split="")

as.numeric(strsplit(test_string,split="")[[1]])*control_2_11_vector

string_vector = c("12354123456","93185672104")

pid_control(string_vector)





### Testing are END -----