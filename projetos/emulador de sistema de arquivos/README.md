# Projeto de um emulador de um sistema de arquivos

Utilize dicionários para simular um sistema de arquivos e ofereça um console (shell) para o usuário manipular arquivos e diretórios a partir de comandos digitados. As operações suportadas pelo console são:
* new "<caminho/nome-do-arquivo>": cria um novo arquivo no diretório especificado no caminho (caminho é opcional)
* del "<caminho/nome-do-arquivo>": remove o arquivo do diretório especificado no caminho (caminho é opcional)
* ls "<caminho>": lista todos os arquivos e diretórios localizados no caminho (caminho é opcional)
* mkdir "<caminho/nome-do-dir>": cria um diretório novo no diretório especificado no caminho (caminho é opcional)
* rmdir "<caminho/nome-do-dir>": remove um diretório existente no diretório especificado no caminho (caminho é opcional)
* cp "<caminho/nome-do-arquivo>" "<caminho-destino>": copia o arquivo para um diretório especificado no destino
* mv "<caminho/nome-do-arquivo>" "<caminho-destino>": move o arquivo para um diretório especificado no destino
* exit: sai do shell

