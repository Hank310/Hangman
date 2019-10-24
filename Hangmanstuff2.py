
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
tries = int(input("How many tries should you have?"))
myList = list(myWord)
count = 0
length = len(myList)
guessList = []
while tries > 0:
	
	tries = tries - 1
	guess = input("Input a letter : ")

	for letter in myList:
		guessList.append("_")

	if guess in  myList:
		print("Letter is in word")
		for x in range(0, length):
			if myList[x] == guess:
			 guessList[x] = guess
	else:
		print("Letter is not in word")
		print("Guessed incorrect:" + guess)
		misses += 1

	if not "_" in guessList:
		print("You Won!  The word was " + myWord)
	else:
		print("You have " + str(tries) + " tries remaining")
	print(HANGMANPICS[misses])
	print(guessList)

	


	