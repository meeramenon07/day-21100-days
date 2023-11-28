import emoji
print("Welcome to the Math Game!")
print("Let us test your multiplication knowledge")
print()
score = 0
for i in range(1,11):
  my_multiples = int(input("Name a number for your multiples: "))
  right_ans = i * my_multiples
  print(i, "X", my_multiples)
  your_ans = int(input("> "))
  if your_ans == right_ans:
    print("You got it Right! Great!")
    score += 1
  else:
    print("No, that's wrong! The right answer should be", right_ans)

  if score == 10:
    print("Wow! You are a Math Giant! You got all the answers right!")
    print(emoji.emojize(":grinning_face_with_big_eyes:"))
  else:
    print("You scored", score, "out of 10 right!")
  

     
     


    
    

          
  

      
    
  


  


