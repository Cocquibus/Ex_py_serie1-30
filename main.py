def exercice1():
    def e_potentielle(masse,hauteur,longeur,largeur,e_limite,g=9.81):
        E = masse * hauteur * longeur * largeur * g
        print("la puissance limite est de ",e_limite," et le E est de ",E)
        #on aurait pu retourner juste E < e_limite pour trouver si oui ou non c'est plus petit pour éviter autant de code.
        if(E >= e_limite):
            print("le E est donc plus élevé que la limite")
        else:
            print("la limite est plus élevé que le E")

    def puissancelimite(puissance):
        P = puissance ** 2
        return P 

    puissance = puissancelimite(240)
    e_potentielle(120,3,5,2,puissance)