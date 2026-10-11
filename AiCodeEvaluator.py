# Addiation AI tester

def AI_Addiation(a,b):
   #return a+b     "If you want to real output of AI then uncomment That code line" 
    return a-b    # AI giving the wrong retrn value that is subtraction in case od addiation.


def AI_Addiation_Tester():
    input_a=10
    input_b=5
    expected_output=15   # If you want to give real input then change expected_output=input_a+input_b

    ai_output=AI_Addiation(input_a,input_b)
    print("-------1.Addiation Test Start")

#code for normal input 
    if expected_output==ai_output:
        print(f"Addiation Testing result is pass. Addiation is correct")
    else:
        print(f"Addiation Testing Fail.Expected output is {expected_output}, but AI gives {ai_output}\n")  

# Code for Ege OUtput for un-expected or an normal input
    edge_output = AI_Addiation(-5, -10)
    print(f"Edge Case (-5 + -10) -> AI Gives: {edge_output} | Expexted= -15")
        
    if ai_output == 15 and edge_output == -15:
         print("Edge case result PASS!")
    else:
        print("Edge case result Fail! (AI does not handle edge case poperly)")      


AI_Addiation_Tester()

print("----------------------------------------------------------")

# Character Counting Test Code

def Ai_Counter(text):
    return 6    #For real  Ai change return 6 into return len(text)

def Ai_Counter_Tester():
    word="Akshay"
    expected_output=5   #For real  Ai output expected_output=5 into expected_output=len(word)

    Ai_output=Ai_Counter(word)

    print("----------2.Character Counting test start")
# Code For Edge Case HAndling in Normal condiation

    if expected_output==Ai_output:
        print("Character Counting Test pass, answer is correct")
    else:
        print(f"Character Counting Test fail,because ecpected output is {expected_output}, and ai gives {Ai_output}")

# Code For Edge Case HAndling in abnormal condiation

    edge_output = Ai_Counter("")
    print(f"Edge Case (Empty String) -> AI Giving: {edge_output} | Expexted: 0")
    
    if Ai_output == 6 and edge_output == 0:
        print("Result PASS\n")
    else:
        print("Result FAIL (AI does not handle blank string properly)\n")

    
 
Ai_Counter_Tester()