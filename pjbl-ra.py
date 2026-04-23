# Menu de opcões
opcao = -1
indice_imc = "IMC não calculado"
meta_agua = "Meta de água não calculada"
falta_de_ml = "Quanto falta para bater a meta n foi calculado"
gasto_final = "Gasto calórico não calculado"
meta_diaria = "Meta diária de exercício não calculado"

# Início do menu
while opcao != 0:
    print('\n1- Saber meu imc.')
    print('2- Meta diária de água.')
    print('3- Gasto calórico')
    print('4- Meta de exercicios')
    print('5- Resumo total.')
    print('0- Encerrar programa.')
    opcao = int(input('Digite a opção desejada:'))

    # IMC
    if opcao == 1:
        print('\n------------Vocé escolheu saber seu imc!------------\n')
        peso = float(input('Qual é o seu peso em kg?'))
        altura = float(input('Qual é sua altura em metros? (Utilize ponto ao invés de vírgula. Ex: 1.70)'))

        imc = peso / (altura ** 2)
        indice_imc = imc
        print('Seu imc é de :' , imc)

        if imc < 18.5:
            print('e você está abaixo do peso.')
        elif imc >= 18.5 and imc <= 24.9:
            print('e você está no peso ideal.')
        elif imc >= 25 and imc <= 29.9:
            print('e você está sobrepeso.')
        elif imc >= 30 and imc <= 34.9:
            print('e você está com obesidade grau 1.')
        elif imc >= 35 and imc <= 39.9:
            print('e você está com obesidade grau 2.')
        else:
            print('e você está com obesidade grau 3.')



    # Água diária
    elif opcao == 2:
        print('\n------------Você escolheu saber sobre sua meta de água!------------\n')
        print('1- Quantos ml de água devo beber?')
        print('2- Quantos ml falta para bater a meta diária de água?')

        opcao_agua = int(input('Digite a opção que deseja saber:'))

        if opcao_agua == 1:
            peso = float(input('Digite seu peso em kg:'))
            agua = peso * 35
            print('Você deve beber', agua, 'ml por dia!')
            meta_agua = agua
        elif opcao_agua == 2:
            peso = float(input('Digite seu peso em kg:'))
            agua = peso * 35
            falta_ml=0
            ml = float(input('Digite quantos ml você tomou hoje:'))
            falta_ml = agua - ml
            print('Você deve tomar', falta_ml, 'ml hoje!')
            falta_de_ml = falta_ml
        else:
            print('Opção inválida')

    # Gasto calórico
    elif opcao == 3:
        print('\n------------Você escolheu saber o gasto calórico de cada atividade------------\n')
        print('1- Caminhada leve (4 km/h)')
        print('2- Ciclismo (16 km/h)')
        print('3- Musculação ')
        print('4- Corrida (8-10 km/h)')
        print('5- Natação')
        print('6- Pular corda')
        met = 0
        opcao_met = int(input('digite a o número da atividade que você praticou:'))

        peso = float(input('digite seu peso em kg:'))
        tempo = float(input('digite quanto tempo você praticou a atividade física em horas:'))
        gasto_calorico = peso * tempo * met

        if opcao_met == 1:
            met = 2
            gasto_final = gasto_calorico
        elif opcao_met == 2:
            met = 4
            gasto_final = gasto_calorico
        elif opcao_met == 3:
            met = 5
            gasto_final = gasto_calorico
        elif opcao_met == 4:
            met = 8
            gasto_final = gasto_calorico
        elif opcao_met == 5:
            met = 10
            gasto_final = gasto_calorico
        elif opcao_met == 6:
            met = 12
            gasto_final = gasto_calorico
            print('Seu gasto calórico foi de:', gasto_calorico, 'kcal')
        else:
            print('Opção inválida!')



    # Meta diária de exercicios
    elif opcao == 4:
        print('\n------------Você escolheu checar a meta diária de exercícios!------------\n')
        print('Qual seu objetivo fazendo exercícios físicos?')
        print('1- Manter a saúde em dia')
        print('2- Emagrecimento')
        print('3- Ganhar massa muscular')

        opcao_objetivo = int(input('Digite a opção: '))

        if opcao_objetivo == 1:
            print('Objetivo: Manter a saúde')
            peso = float(input('Digite seu peso em kg: '))
            if peso <= 60:
                meta_diaria = 'Você deve se exercitar 20/25 minutos por dia'
                print(meta_diaria)
            elif peso < 75:
                meta_diaria = 'Você deve se exercitar 25/35 minutos por dia'
                print(meta_diaria)
            elif peso < 90:
                meta_diaria = 'Você deve se exercitar 30/40 minutos por dia'
                print(meta_diaria)
            elif peso < 110:
                meta_diaria = 'Você deve se exercitar 45 minutos por dia'
                print(meta_diaria)
            else:
                meta_diaria = 'Você deve se exercitar 50 minutos por dia'
                print(meta_diaria)

        elif opcao_objetivo == 2:
            print('Objetivo: Emagrecimento')
            peso = float(input('Digite seu peso em kg: '))
            if peso <= 60:
                meta_diaria = 'Você deve se exercitar 30/40 minutos por dia'
                print(meta_diaria)
            elif peso < 75:
                meta_diaria = 'Você deve se exercitar 35/45 minutos por dia'
                print(meta_diaria)
            elif peso < 90:
                meta_diaria = 'Você deve se exercitar 40/50 minutos por dia'
                print(meta_diaria)
            elif peso < 110:
                meta_diaria = 'Você deve se exercitar 45/60 minutos por dia'
                print(meta_diaria)
            else:
                meta_diaria = 'Você deve se exercitar 50/70 minutos por dia'
                print(meta_diaria)

        elif opcao_objetivo == 3:
            print('Objetivo: Ganhar massa muscular')
            peso = float(input('Digite seu peso em kg: '))
            if peso <= 60:
                meta_diaria = 'Você deve fazer 40/60 minutos de musculação'
                print(meta_diaria)
            elif peso < 75:
                meta_diaria = 'Você deve fazer 45/60 minutos de musculação'
                print(meta_diaria)
            elif peso < 90:
                meta_diaria = 'Você deve fazer 50/70 minutos de musculação'
                print(meta_diaria)
            elif peso < 110:
                meta_diaria = 'Você deve fazer 50/75 minutos de musculação leve'
                print(meta_diaria)
            else:
                meta_diaria = 'Você deve fazer 40/60 minutos de musculação leve'
                print(meta_diaria)


        else:
            print("Opção invalida!")



    # Resumo diário
    elif opcao == 5:
        print('------------RESUMO DIÁRIO------------')
        print('Seu imc é de: ' , indice_imc)
        print('Você deve beber ' , meta_agua , ' ml')
        print('Faltam' , falta_de_ml , 'ml' 'para bater a meta')
        print('Seu gasto calórico foi de: ' , gasto_final)
        print(meta_diaria)


    # Encerra o programa
    elif opcao == 0:
        print('Até a próxima!')

    # Apenas opções do menu
    else:
        print("Digite uma opção válida!\n")