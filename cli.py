# # -*- coding: utf-8 -*-
# parte principal do programa
# Cria comandos a ser recebidos pelo terminal(cmd)
#
#
# Autor Junior
# Projeto PWD


from program import computer, cpu, memory, tools, disk, network
import sys


params = sys.argv

# Analisa os arg recebidos pelo teminal(cmd)

if len(params) > 1:

    # Apresenta o OS a a Versão
    if params[1] == 'os' or params[1] == 'system':
        print("sistema operacional", computer.so())
        print("versão:", computer.osVersion())


    # Apresenta o nome do OS na rede
    elif params[1] == 'name':
        print('nome de rede:', computer.name())


    # Apresenta se Linux, a distro
    elif params[1] ==  'distro':
        print('distribuição:', computer.distro())


    # Apresenta o processador da maquina
    # recebe dois parametros
    # persentage: mostra quanto esta sendo consumido e livre
    # benchmarking n: mostra o desempenho do cpu por n vezes
    elif params[1] == 'process' or params[1] == '-p':
        if len(params) == 4 and params[2] == 'parcentage' and int(params[3]) >= 1:
            for x in  range(int(params[3])):
                consume = cpu.percentage()
                print('comsumindo',consume.user + consume.system, "%")
                print('Livre:', str(consume.idle)+"%")

                print("-" * 10)

        elif len(params) == 4 and params[2] == 'benchmarking' and int(params[3]) >= 1:
            media = 0
            for x in range(int(params[3])):
                consume = cpu.percentage()
                media += consume.user + consume.system

            media = media/int(params[3])
            print("Media de consumo da cpu durante", params[3],'segundos:', str(media)[:5] + "%")

        else:
            print('processador:', computer.cpu())
            print('velocidade:', cpu.freq())
            print('cores:', cpu.cores())
            print('Cores fisicos: ', cpu.phy_cores())


    # Apresenta a memoria(ram) da maquina obrigado a tem ao menos 1 para
    # memory recebe size; percentage; free; used
    # size: mostra o tamanho total da memoria
    # percentage: mostra a porcentagem de memoria sendo usada
    # free: mostra a quantidade de memoria livre
    # used: quantidade de memoria sendo usada
    elif params[1] == 'memory' or params[1] == '-m':
        if str(params).find('size') > 0:
            print("Tamanho da memoria", memory.size(),"GBs")

        if str(params).find("percentage") > 0:
            print("Consumo atual de memoria", str(memory.percentage())+"%")

        if str(params).find("free") > 0:
            print("Memoria Livre:",memory.free(),"GBs")

        if str(params).find("used") > 0:
            print("Memoria sendo usada:", memory.used(), "GBs")


    # Disk recebe info e mostra quantos discos disponiveis e apresenta-os
    elif params[1] == "disk" or params[1] == '-d':
        if str(params).find("info") >0:
            disklint = disk.info()
            i = 0
            print("Nº de discos", len(disklint))
            while i < len(disklint):
                print("="*20)
                print("ponto de montagem:", disklint[i].mountpoint)
                print("sistema de arquivos:", disklint[i].fstype)
                i += 1


    # network recebe (bytes, packs)
    # bytes: quantidade de bytes eviados e recebidos
    # packs: quantidade de pacotes enviados e recebidos
    elif params[1] == 'network' or params[1] == '-n':
        if str(params).find("bytes") > 0:
            bytes_network = network.info()

            print("Bytes enviados:", round(bytes_network.bytes_sent/1024**3,3),"GBs")
            print("Bytes recebidos:", round(bytes_network.bytes_recv/1024**3,3),"GBs")

        if str(params).find("packs") > 0:
            bytes_network = network.info()
            print("Pacotes enviados:", round(bytes_network.packets_sent/1024**3,5))
            print("Pacotes recebidos:", round(bytes_network.packets_recv/1024**3,5))



    # Apresenta apresenta a arquitetura da maquina
    elif params[1] == 'arc':
        print('Arqutetura da maquina:', computer.arc())


    # Desliga a maquina
    elif str(params).find("shutdown") > 0:
        print("Desligando computador.....")
        tools.shutdown()

    # Reinicia a maquina
    elif str(params).find("reboot") > 0:
        print("Reiniciando computador....")
        tools.reboot()


    else:
        print("parametro desconhecido")

else:
    print("sistema operacional", computer.so())
