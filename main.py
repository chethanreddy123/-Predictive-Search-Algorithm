import streamlit as st
from fast_autocomplete import AutoComplete

ListOfWords = ['Abdominal pain',
 'Abdominal redness',
 'Abdominal swelling',
 'Abnormal sweating',
 'Acne',
 'Allergy',
 'Anal Fissure',
 'Anal pain',
 'Anemia',
 'Anhedonia',
 'Ankle pain',
 'Anxiety',
 'Appendicitis',
 'Arm pain',
 'Arm swelling',
 'Arm weakness',
 'Armpit pain',
 'Armpit swelling',
 'Attention deficit',
 'Back pain',
 'Bad breath',
 'Bad or bitter taste',
 'Black or tarry stool',
 'Bladder Infection (UTI)',
 'Blood in stool',
 'Blood in urine',
 'Blurry vision',
 'Bronchitis',
 'Bulging eye',
 'Burning or painful urination',
 'Buttocks pain',
 'Calf pain',
 'Calf swelling',
 'Cheek pain',
 'Cheek swelling',
 'Chest pain',
 'Chills',
 'Confusion',
 'Constipation',
 'Cool bluish skin',
 'Cough',
 'COVID-19',
 'Decreased appetite',
 'Decreased hearing',
 'Decreased urination',
 'Decreased vision',
 'Dental pain',
 'Diarrhea',
 'Difficulty urinating',
 'Dizziness',
 'Drooping eyelid',
 'Dry mouth',
 'Dry mucous membranes',
 'Dry skin',
 'Ear discharge',
 'Ear pain',
 'Ear pressure',
 'Ear swelling',
 'Elbow pain',
 'Emotional stress',
 'Erectile dysfunction',
 'Excessive thirst',
 'Excessive urination',
 'Eye deviation',
 'Eye discharge',
 'Eye dryness',
 'Eye floaters',
 'Eye Infection',
 'Eye pain',
 'Eye redness',
 'Eyelid pain',
 'Eyelid redness',
 'Eyelid swelling',
 'Facial droop',
 'Facial lesions',
 'Facial numbness or tingling',
 'Facial pain',
 'Facial swelling',
 'Fainting (passing out)',
 'Fatigue',
 'Feeling cold',
 'Feeling down',
 'Feeling faint',
 'Fever',
 'Finger discoloration',
 'Finger pain',
 'Flank pain',
 'Flashing lights in vision',
 'Flatulence',
 'Food Poisoning',
 'Foot fungus',
 'Foot numbness or tingling',
 'Foot pain',
 'Foot redness',
 'Foot sores',
 'Foot swelling',
 'Forearm pain',
 'Foreign body in the eye',
 'Frequent burping',
 'Frequent night urination',
 'Frequent urination',
 'Gastroenteritis',
 'Genital lesions',
 'Goiter',
 'Groin pain',
 'Groin swelling',
 'Hair loss',
 'Hand numbness or tingling',
 'Hand pain',
 'Hand redness',
 'Hand swelling',
 'Headache',
 'Heart palpitations']


# print("The Total Lenght of the List is:",len(ListOfWords))

words = {}

for word in ListOfWords:
    words[word] = {}
        
# print(words)

st.title("Welcome to DocPlus", anchor=None)
st.header("Please Do Enter your Symptoms ", anchor=None)


autocomplete = AutoComplete(words=words)




autocomplete.search(word='arm', max_cost=4, size=3)

selected = st.text_input("")
KeyWords = autocomplete.search(word=selected, max_cost=3, size=3)
NewKeyWords = []
for i in KeyWords:
    NewKeyWords.append(str(i[0]))

st.selectbox("Search",NewKeyWords, index=0)
print(KeyWords)