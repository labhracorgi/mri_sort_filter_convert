#### PID check: 

## Read file:

#help(read.csv)
pid_csv = read.csv()

library(xlsx) #https://cran.r-project.org/web/packages/xlsx/xlsx.pdf
pid_xlsx = read.xlsx()

PIDs = ###SET THIS EQUAL TO PID vector###

#################################### PID CONTROL FUNCTION:  
pid_control = function(p_vector,scan_year_vector){ #Require PID vector and scan time (year) vector.
  
  ##Constant verification vectors: http://www.fnrinfo.no/Teknisk/KontrollsifferSjekk.aspx , https://no.wikipedia.org/wiki/F%C3%B8dselsnummer
  control_1_10_vector = c(3,7,6,1,8,9,4,5,2,1)
  
  control_2_11_vector = c(5,4,3,2,7,6,5,4,3,2,1)
  
  #Booleans:
  bool1 = FALSE
  bool2 = FALSE
  
  #Assuming vector:
  n = length(p_vector)
  
  #Initialise return:
  results_matrix = matrix(0,nrow = n,ncol = 5)
  
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
    
    #Determining gender: (Make sure the ninth number is fed forward.)
    this_is_male = determine_gender(split_pid[9])
    
    #Determining age: (Make sure to only include the first 9.)
    this_age = determine_age(split_pid[c(1:9)],scan_year_vector[i]) ###Need this input...
    
    #Storing everything:
    results_matrix[i,1] = i
    results_matrix[i,2] = this_pid_conlusion
    results_matrix[i,3] = is_corrected
    results_matrix[i,4] = this_is_male
    results_matrix[i,5] = this_age
  }
  
  #Returning result:
  colnames(results_matrix) <- c("Nr","OK","Corrected","isMale","Age")
  
  results_matrix = as.data.frame(results_matrix)
  results_matrix$PID = p_vector
  
  return(results_matrix)
}
#################################### END PID CONTROL FUNCTION.  

#################################### PID AGE GENDER FUNCTION:
determine_gender = function(ix){
  #ix defined as the ninth number.
  
  man_true = FALSE
  
  if((ix %% 2) != 0){ #Checking for if man in this test. https://no.wikipedia.org/wiki/F%C3%B8dselsnummer
    man_true = TRUE
  }
  
  return(man_true)
}

determine_age = function(num_vector,ref_age){
  #Assume num_vector contains 1 to 9 numbers.
  pre_1900 = FALSE
  
  ##Ref age should be between "10-18" in INT format or character.
  age_reference = as.character(ref_age) #Or does this really have to be checked up against which year they were scanned?
  this_age = 0
  
  #Splitting into meaningful categories.
  last_three = num_vector[c(7:9)]
  
  two_day = num_vector[c(1:2)]
  two_month = num_vector[c(3:4)]
  two_year = num_vector[c(5:6)]
  
  #Century check:
  if(
      ((last_three[1] >= 5) & (last_three[1] <= 7))
        & ((last_three[2] >= 0) & (last_three[2] <= 4))
        & ((last_three[3] >= 0) & (last_three[3] <= 9))
      ){ #500-749 are born before 1900
    pre_1900 = TRUE
  }
  
  #Calculating age at time of scan:
  two_year_char = as.character(two_year)
  fifth_sixth_year = paste(two_year_char[1],two_year_char[2])
  if(pre_1900){
    this_age = as.numeric(paste("20",age_reference)) - as.numeric(paste("18",fifth_sixth_year))
    #Case: Scanned in 20XX and born in 18XX
  }else{
    this_age = as.numeric(paste("20",age_reference)) - as.numeric(paste("19",fifth_sixth_year))
    #Case: Scanned in 20XX and born in 19XX
  }
  
  #Infeasible age check:
  if(this_age < 40){ #Theoretical lower limit in our sample.
    warning("There is an individual with the wrong age..! [Too low!]")
    warning("Returing with -1")
    return(-1)
  }
  if(this_age > 150){ #Theoretical upper limit per presupositions in deciding century.
    warning("There is an individual with the wrong age..! [Too high!]")
    warning("Returing with -1")
    return(-1)
  }
  
  return(this_age)
}

#################################### END PID AGE GENDER FUNCTION.

### Testing area: (Seems to work ok)

test_string = "12354123456"

test_split = strsplit(test_string,split="")

as.numeric(strsplit(test_string,split="")[[1]])*control_2_11_vector

string_vector = c("12354123456","93185672104")

pid_control(string_vector)





### Testing are END -----