import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False 


    answers['(c) Weight update'] = "0.5 * math.log((1 - p) / p)"

    
    answers['(d) Weight influence'] = 1.527
    return answers



#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No'

    # type: explain_string
    answers['Explain'] = "No, Alan's approach is not reliable. By mixing classifiers that perform better collectively than at random, ensemble approaches enhance prediction. Flipping coins is a random activity that lacks predictive ability and doesn't make use of stock market knowledge."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "No, C2 is not superior because there is no improvement in class distinction between the two classifiers, as seen by their placement on the ROC curve's random guess line."

   
    answers['(c) Which metric?'] = 'precision/recall' 

    # type: explain_string
    answers['(c) explain'] = "Because C2 has a greater recall, precision and recall measures make it appear superior; nevertheless, this assessment ignores the improvement in FPR, which is crucial for the overall performance of the classifier."
    return answers



#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = " C1 has a very low recall compared to C2 so C2 is considered as the best classifier when compared to C1"

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] =  'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "The right measures to use are precision, recall, and F1-Measure because they offer a fair assessment of the classifier's capacity to identify positive cases with accuracy while reducing false positives—a critical aspect of assessing performance on unbalanced datasets."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 seems to be the best option among C1 and C3 due to its higher precision and better F1-measure, which indicates a more balanced performance regarding false positives and false negatives. C3's performance is especially relevant if the cost of false positives is high because it maintains a relatively low FPR while improving precision."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "0.1*p" 

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "(2*0.1*p)/(0.1+p)" 

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'yes'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers



#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 0.5333,
        'precision': 0.6154,
        'F-measure': 0.5714,
        'accuracy': 0.88
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure' 

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy' 

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] ="The F-measure is the best of the three metrics since it combines recall and precision into one. Because accuracy merely counts total errors without taking type into account (such as the distinction between false positives and false negatives), it can be deceptive when classes are unbalanced."
    return answers

#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The utilization of TPR/FPR is recommended due to its emphasis on the significance of accurately detecting positive instances, or true positives, while avoiding false positives. This is particularly important for cancer detection tests, as failing to identify a positive case can have dire repercussions."


    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "Since the F1 measure strikes a compromise between recall and precision, it minimizes both false positives and false negatives, making it the preferred option when the repercussions of false positives are severe and could result in further medical procedures, unneeded stress, or other bad outcomes."
    

    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
