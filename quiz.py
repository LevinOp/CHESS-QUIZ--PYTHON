def quiz():
           while True:
                score=0
                print('Wellcome to my chess quiz!!')
                print('Lets start!!')
                    
                q1 = (input("How many pawns white has at the start of the game? : "))
                if q1 == '8':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q2 = (input("How many square does a chess board have? : "))
                if q2 == '64':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q3= input('Where was chess originated? : ')
                if q3.lower() == 'india':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q4  =  str(input('Which pice is on H8? : '))
                if q4.lower() == 'rook':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q5 = input('If a king has no square to go and he is in check is called? : ')   
                if q5.lower() == 'checkmate':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q6 = input('If a king has no square to go and no other legal move what is it called? : ')
                if q6.lower() == 'stalemate':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q7 = input('What is a spical pawn move is called? : ')
                if q7.lower() == 'enpasent':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q8 = input('Is two kinght and king endgame a draw?: ')
                if q8.lower() == 'yes':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q9 = input('Is two bishop and a king endgame a draw?: ')
                if q9.lower() == 'no':
                    print('correct!!')
                else:
                    print('incorrect :(')
                    score+=1
                q10 = input("Who do u think is the best player? : ")
                print(f'So u think {q10} is the best,uhh!')

                print(f'Your got {score} worong out of 9')
                
                restart = input('Want to play again? (the questions would be the same!) yes/no :')
                if restart != 'yes' 'y':
                  break

quiz()

# THIS IS MY FIRST PYTHON PROJECT HOPE U HAD FUN PLAYING IT 