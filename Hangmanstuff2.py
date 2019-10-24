
import random
HANGMANPICS = ['''


   +---+

   |   |

       |

       |

       |

       |

 =========''', '''

   +---+

   |   |
   0
       |

       |

       |

       |

 =========''', '''

   +---+

   |   |
   0
   I   |

       |

       |

       |

 =========''', '''

   +---+

   |   |
   0
  -I   |

       |

       |

       |

 =========''', '''

   +---+

   |   |
   0
  -I-  |

       |

       |

       |

 =========''', '''

   +---+

   |   |
   0
  -I-  |
  /
       |

       |

       |

 =========''', '''

  +---+

   |   |
   0
  -I-  |
  / \
       |

       |

       |

 =========''']

misses = 0
myWord = "hello"
noList = []
myList = list(myWord)
count = 0
length = len(myList)
guessList = []
tries = len(myList) + int(input("How many extra misses should you have?"))
while tries > 0:
	
	guess = input("Guess a letter : ")

	for letter in myList:
		guessList.append("_")

	if guess in  myList:
		count = 0
		for letter in myList:
			if letter == guess:
				guessList[count] = guess
			count += 1
	else:
		print("Letter is not in word")
		print("Guessed incorrect : " + guess)
		misses += 1
		tries = tries - 1
		no2List = noList.append(guess)

	print(HANGMANPICS[misses])
	guessList = guessList[:len(myList)]
	print(guessList)
	print("Missed letters : " + str(noList))
	if not "_" in guessList:
		print("You Won! The word was " + myWord)
		break
	else:
		print("You have " + str(tries) + " misses remaining")
	if tries == 0:
		print("Game over, you lost")
		break


	