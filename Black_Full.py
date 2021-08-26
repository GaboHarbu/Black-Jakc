import random

#Mientras juego=1 se va a poder jugar otra partida

juego=1

print ('Bienvendio al casino de Gabo!')
    
print('')
    
nombre_jugador=input('Como quiere que le llamemos? ')
    
print('')
    
print('En esta variante del Black Jack la carta A tiene un valor numerico de 11 en las primeras dos rondas, luego puede valer 1 o 11  depeniendo de lo que decidas! ')
    
print('')
    
print('Comenzemos!')
    
print('')
    

while juego==1:
    
    
    
    
    numero_cartas=[2,3,4,5,6,7,8,9,10,'K','Q','J','A']
    palo_cartas=['♣', '♧', '♥', '♡', '♦', '♢', '♠', '♤']
    
    
    #Cartas del jugador
    carta1_jugador=[random.choice(numero_cartas),  random.choice(palo_cartas) ]
    carta2_jugador=[random.choice(numero_cartas), random.choice(palo_cartas) ]


    #Cartas del casino
    carta1_casino=[random.choice(numero_cartas), random.choice(palo_cartas) ]
    carta2_casino=[random.choice(numero_cartas), random.choice(palo_cartas) ]

    
    print('El crupier tiene: ')
    print('')
    print (carta1_casino)
    print (carta2_casino)

    print('')
    print('{} tiene: '.format(nombre_jugador))
    print('')
    print (carta1_jugador)
    print (carta2_jugador)
    
    def valor_cartas_jugador(carta1_jugador, carta2_jugador):
        
        if carta1_jugador[0]  == ('K'):
            carta1_jugador[0]= 10
        elif carta1_jugador[0]  == ('Q'):
            carta1_jugador[0]= 10
        elif carta1_jugador[0]  == ('J'):
            carta1_jugador[0]= 10
    
    
        if carta2_jugador[0]  == ('K'):
            carta2_jugador[0]= 10
        elif carta2_jugador[0]  == ('Q'):
            carta2_jugador[0]= 10
        elif carta2_jugador[0]  == ('J'):
            carta2_jugador[0]= 10
    
        if carta1_jugador[0]  == ('A'):
            carta1_jugador[0]=11 
        elif carta2_jugador[0]  == ('A'):
            carta2_jugador[0]=11 
            
            
        
    def valor_cartas_casino(carta1_casino, carta2_casino):
        
        if carta1_casino[0]  == ('K'):
            carta1_casino[0]= 10
        elif carta1_casino[0]  == ('Q'):
            carta1_casino[0]= 10
        elif carta1_casino[0]  == ('J'):
            carta1_casino[0]= 10
    
    
        if carta2_casino[0]  == ('K'):
            carta2_casino[0]= 10
        elif carta2_casino[0]  == ('Q'):
            carta2_casino[0]= 10
        elif carta2_casino[0]  == ('J'):
            carta2_casino[0]= 10
    
        if carta1_casino[0]  == ('A'):
            carta1_casino[0]=11 
        elif carta2_casino[0]  == ('A'):
            carta2_casino[0]=11 
            
            
    valor_cartas_jugador(carta1_jugador, carta2_jugador)
    
    valor_cartas_casino(carta1_casino, carta2_casino)
    
    #Puntajes despues de la primera mano
    
    puntaje_casino=carta1_casino[0] + carta2_casino[0]
    
    
    puntaje_jugador=carta1_jugador[0] + carta2_jugador[0]
    
    
    
    #Funcion para jugar de nuevo no
    
    def juego():
        juego=int(input('¿Quiere jugar otra vez? presione 1 para seguir jugando o presione 2 para salir del juego. '))
        
    #Blackjacks
    
    if puntaje_jugador== 21:
        print ('BlackJack! de {}'.format(nombre_jugador))
        print ('Ganste!')
        
        juego()
        

    
    
    if puntaje_casino== 21:
        print ('BlackJack de la casa!')
        print ('Perdiste!')
        
        juego()
        
        
        
        
        
    if puntaje_jugador<21 and puntaje_casino!=21 :
        segunda_ronda_jugador=int(input('Quiere  plantarse con {} o quiere pedir otra carta? presione 1 para plantarse, presione 2 para pedir otra carta. '.format(puntaje_jugador)))
        
        
        
        
        #El Jugador se planta en la primera ronda
        if segunda_ronda_jugador==1:
            
            print ('El jugador se plantó con {} '.format(puntaje_jugador))
            
            while puntaje_casino<=16:
            
                print('')
                print('El crupier pidió otra carta ')
                print('')
                
                carta3_casino=[random.choice(numero_cartas), random.choice(palo_cartas)]
              
                print(carta3_casino)
                
                if carta3_casino[0]  == ('K'):
                    carta3_casino[0]= 10
                elif carta3_casino[0]  == ('Q'):
                    carta3_casino[0]= 10
                elif carta3_casino[0]  == ('J'):
                    carta3_casino[0]= 10
                elif carta3_casino[0]  == ('A'):
                    if puntaje_casino+11 >21:
                        carta3_casino[0]=1
                        
                    elif puntaje_casino+11 <= 21:
                        carta3_casino[0]=11
                            
                puntaje_casino= puntaje_casino + carta3_casino[0]
            
            if puntaje_casino>=16:
                print ('El crupier se plantó con {} '.format(puntaje_casino))
                
                
                #Resultados
                
                
                if puntaje_casino>puntaje_jugador and puntaje_casino<=21 :
                    print('El croupier ganó con {}, mejor suerte la proxima. '.format(puntaje_casino))
                    juego()
                
                elif puntaje_casino<puntaje_jugador and puntaje_casino<=21 :
                    print('{} ganó con {}, Felicidades! '.format(nombre_jugador, puntaje_jugador))
                    juego()
                    
                elif puntaje_casino==puntaje_jugador and puntaje_casino<=21 :
                     print('{} ganó con {}, Felicidades! '.format(nombre_jugador, puntaje_jugador))
                     juego()
                     
            if puntaje_casino>21 :
                print('El crupier se pasó, perdió la casa, el ganador es  {}. '.format(nombre_jugador))
                juego()
                
                
            
            
            
            
          #El Jugador pide otra carta
        if segunda_ronda_jugador==2:
            
            puntaje_final_jugador=[]
            
            otra_ronda=1
            
            
            while otra_ronda==1:
                 
                carta3_jugador=[random.choice(numero_cartas), random.choice(palo_cartas)]
            
                print('')
            
                print('{} recibió '.format(nombre_jugador))
            
                print(carta3_jugador)
                
                print('')
                if carta3_jugador[0]  == ('K'):
                    carta3_jugador[0]= 10
                
                elif carta3_jugador[0]  == ('Q'):
                    carta3_jugador[0]= 10
                
                
                elif carta3_jugador[0]  == ('J'):
                    carta3_jugador[0]= 10
                
                if carta3_jugador[0]  == ('A'):
                
               
                    a_jugador1=int(input('Cuanto quiere que valga su A: 1 o 11:  '))
               
                    carta3_jugador[0]=a_jugador1
            
            
                puntaje_jugador= puntaje_jugador+ carta3_jugador[0]
                
               
                
                if puntaje_jugador<=21:
                    otra_ronda=int(input('¿Desea pedir otra carta, o desea plantarse con {}? presione 1 para pedir otra carta o presione 2 para plantarse. '.format(puntaje_jugador)))
            
                if puntaje_jugador>21:
                    print('Te pasaste con {}, mejor suerte la proxima'.format(puntaje_jugador))
                    juego()
                   
            
                
            
              
            while puntaje_casino<=16:
                
            
                print('')
                print('El crupier pidió otra carta ')
                print('')
                
                carta3_casino=[random.choice(numero_cartas), random.choice(palo_cartas)]
              
                print(carta3_casino)
                print('')
                if carta3_casino[0]  == ('K'):
                        carta3_casino[0]= 10
                elif carta3_casino[0]  == ('Q'):
                        carta3_casino[0]= 10
                elif carta3_casino[0]  == ('J'):
                        carta3_casino[0]= 10
                if carta3_casino[0]  == ('A'):
                    if puntaje_casino + 11 >21:
                            carta3_casino[0]=1
                    elif puntaje_casino + 11 <= 21:
                            carta3_casino[0]=11
                    
                        
                puntaje_casino=puntaje_casino + carta3_casino[0]
            
            if puntaje_casino>21 :
                print('El crupier se pasó, perdió la casa, el ganador es  {}. '.format(nombre_jugador))
                juego()

            
            
            if puntaje_jugador<=21 and puntaje_casino<=21 :
                
               
                if otra_ronda==2:
                   
                    if puntaje_jugador>puntaje_casino:
                       
                        print('El ganador es {} con {} ! '.format(nombre_jugador, puntaje_jugador))
                        juego()

                    elif puntaje_jugador<puntaje_casino:
                        print('El ganador es el crupier con {} ! '.format(puntaje_casino))
                    
                        juego()
                                                                                                                                                            
                                                                                                                                                                
                                                                                                                                                                
print('Gracias por jugar! Hasta la proxima!')                                                                                                                                      
exit()     

        

