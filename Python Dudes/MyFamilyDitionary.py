print('Input any of these name: Ashmit, Ritika, Rishabh, Sarita, Jai Prakash')
inputna = input("Enter an name from above and I will give his/her status: ")
dicto = {"Ashmit":"Smallest Son","Ritika":"Daughter", "Rishabh":"Elder Son", "Sarita":"Mother", "Jai Prakash":"Father"}
inputname = inputna.capitalize()
print(dicto[inputname])
