#JOGO ADIVINHAÇÃO
palavra_certa = "torta"
print("Vamos jogar um jogo!!!")
print()
print("Tente adivinhar a palavra.")
print("Você tem 3 chances para adivinhar.")
print("A cada erro, aparece uma dica nova.")
print()
print("DICA1: Comida")
palavra = input("Tentativa1: ")



if palavra == palavra_certa:
  print()
  print("Parabens, você acertou!")

elif palavra != palavra_certa:
  print()
  print()
  print("Você errou :C")
  print("Tente novamente")
  print("DICA2: É assada!")
  palavra = input ("Tentativa2: ")
  
  if palavra == palavra_certa:
    print()
    print("Parabens, você acertou!")
    
  elif palavra != palavra_certa:
      print()
      print()
      print("Você errou :C")
      print("Tente novamente")
      print("DICA3: Existem vários sabores, mas a mais conhecida é a de   frango.")
      palavra = input ("Tentativa3: ")

    
      if palavra == palavra_certa:
        print()
        print("Parabens, você acertou!")
      elif palavra != palavra_certa:
        print()
        print()
        print("Você errou :C")
        print("Ultima chance!!!!")
        print("ULTIMA DICA: Feita geralmente em uma bandeja!")
        palavra = input ("Tentativa final: ")


        if palavra == palavra_certa:
          print()
          print("Parabens, você acertou!")
        else:
          print()
          print()
          print("Você errou :C")
          print("Fim de Jogo.")
          print(f"A palavra certa era: {palavra_certa}.")
