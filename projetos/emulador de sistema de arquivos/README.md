# Projeto de um emulador de um sistema de arquivos

Utilize dicionários para simular um sistema de arquivos e ofereça uma interface de console (shell) para o usuário manipular arquivos e diretórios a partir dos comandos digitados. As operações suportadas pelo console são:
* new <caminho/nome-do-arquivo>: cria um novo arquivo no diretório especificado no caminho (caminho é opcional)
* del <caminho/nome-do-arquivo>: remove o arquivo do diretório especificado no caminho (caminho é opcional)
* ls <caminho>: lista todos os arquivos e diretórios localizados no caminho (caminho é opcional)
* mkdir <caminho/nome-do-dir>: cria um diretório novo no diretório especificado no caminho (caminho é opcional)
* rmdir <caminho/nome-do-dir>: remove um diretório existente no diretório especificado no caminho (caminho é opcional)
* cp [caminho/nome-do-arquivo] [destino]: copia o arquivo para um diretório especificado no destino
* mv <caminho/nome-do-arquivo> <destino>: move o arquivo para um diretório especificado no destino
* exit: sai do shell

 ## Principais requisitos
 * Quando um novo arquuivo é criado (comando new), deve ser atribuído um tamanho de arquivo em bytes cujo valor seja um número inteiro aleatório entre 0 e 8096
 * A saída/resultado de um comando ls deve exibir o total de bytes ocupado pelos arquivos daquele diretório
 * Em todos os comandos, o caminho de origem é um parâmetro opcional. Ou seja, ele pode não existir. Neste caso, o diretório de partida do comando é o diretório atual onde o usuário se encontra
 * Em todos os comandos, o caminho de origem pode ser relativo ou completo. (ex.: caminho relativo para o comando ls: ls ../)
 * Modele o sistema de arquivos de forma orientada a objetos (Dica: pense em uma classe para Arquivo e outra classe para Diretorio)

 ## Planejamento das entregas
 * TP2: Interface de console funcionando com a identificação dos comandos e parâmetros capturados para cada comando (exibindo erro quando for o caso)
 * TP3: Comandos new, ls e mkdir de maneira programática (sem precisar estar integrados ao shell)
 * TP4: Restante dos comandos funcionando (sem precisar estar integrados ao shell)
 * AT: Todos os comandos funcionando integrados à interface de console

