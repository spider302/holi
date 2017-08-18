def NewGame():
	""" Metemos todo en un ciclo while """
	while(True):
		os.system('cls')
		print ('\n')
		print ( ' Muy bien, ¡un nuevo juego!')
		print ( ' Vamos a comenzar \n')
		sleep(1)
		ans = input(' ¿Piedra, Papel o tijera? >> ')
		cpu = random.choice(outcomes)
		sleep(1)
		print (' CPU: '+cpu)
		PaperRockScissor(ans,cpu)
		sleep(1)
		
		aksAgain = input(' Deseas seguir jugando?:  Y/N ')
		""" Verificamos que su respuesta no sea un no, en caso de serlo rompremos el ciclo """
		if aksAgain in ["N","NO","n","noc"]:
			break
