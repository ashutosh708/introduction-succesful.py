b=True
while b==True:
      input("enter your name")
      input("enter your father's name")
      input("enter your mother's name")
      input("enter your brother's name")
      a=int(input("enter your age"))
      if a<18:
            input("in which class do you study")
            b=int(input("what was your percentage last year?"))
            if b>95:
                  print("Outstanding")
            elif b>90:
                  print("excellent")
            elif b>85:
                  print("very good")
            input("enter your school name")
            input("where is your school")
      else:
          input("what do you do")
          input("from where do you do your job/course")

      input("what are your hobbies")
      input("where do you live")

      c=input("Do you want to repeat the program: Yes/No").lower()
      if c=="yes":
            continue
            
      else:
            exit()
