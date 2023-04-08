import time

def new_game():
    guesses=[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print (i)
        guess = input("Alege (A,B sau C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answear(questions.get(key),guess)

        question_num += 1
    display_score(correct_guesses,guesses)

def check_answear(answear,guess):

    if answear == guess:
        print("CORECT!")
        return 1
    else:
        print("GREȘIT!")
        return 0

def display_score(correct_guesses,guesses):
    print("-----------------------------------------------------")
    print("REZULTAT")
    print("-----------------------------------------------------")
    print("Răspunsurile corecte: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Răspunsurile tale: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Scorul tău este "+ str(score) + "%")

print("Acest joc este despre Ingrid")

questions = {
    "1. Care este culoarea preferată? ":"A",
    "2. Care este cartea preferată? ":"C",
    "3. Care este serialul preferat? ":"C",
    "4. Care este filmul preferat? ":"A",
    "5. Care este cocktailul preferat? ":"B",
    "6. Care este ginul preferat? ":"B",
    "7. Cand este aniversarea de ciclu? ":"B",
    "8. Care este floarea preferata? ":"A",
    "9. Cu ce aliment are Ingrid o obsesie uriașă? ":"C",
    "10. La ce oră s-a nascut? ":"A"
}
options = [["A. roșu corai și albastru cerneală","B. roșu corai și verde lime","C. roșu corai și albastru de cobalt închis"],
           ["A. Breasts and Eggs by Mieko Kawakami","B. My Brilliant Friend by Elena Ferrante","C. Giovanni's Room by James Baldwin"],
           ["A. Stranger Things", "B. Peaky Blinders", "C. Dark"],
           ["A. Kill Bill","B. Fight Club", "C. Pulp Fiction"],
           ["A. Aperol Spritz","B. Gin Tonic","C. Martini Fiero"],
           ["A. Ki No Bi Kyoto Dry Gin","B. Monkey 47","C. Seedlip Spice 94"],
           ["A. 10 iulie","B. 20 iulie", "C. 10 august"],
           ["A. Floarea Soarelui","B. Trandafirul Deșertului","C. Laleaua"],
           ["A. Ciuperci","B. Brânză sărată","C. Măsline"],
           ["A. 03:15 AM","B. 09:15 AM","C. 02:30 AM"]]

new_game()
time.sleep(20)
