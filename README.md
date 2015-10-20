# BeachBotEcam
## Eurobot 2015-2016
Projet eurobot 2015-2016 de l'ECAM.

## Liste des commandes utiles pour Git
1. `git status` : permet de lister les modifications réalisées depuis le dernier *commit*.
2. `git add .` : permet d'ajouter tous les fichiers modifiés au futur *commit*. Si vous ne voulez ajouter qu'un seul fichier, il faut aller le préciser avec son nom à la place du **.**. Par exemple `git add fichier.cpp`.
3. `git commit` : permet de créer un nouveau commit avec les fichiers ajoutés précédemment depuis le dernier *commit*. Il faut décrire ce fichier avec une petite phrase. Sauver en faisant **ctrl+x** suivi d'un **y** pour confirmer.
4. `git push origin master` : permet d'uploader vos différents *commit* locaux sur le serveur.
5. `git pull <url>` : permet de récupérer les fichiers qui se trouve dans votre *repository* sur le serveur (par défaut le vôtre). Si vous voulez rechercher les fichiers qui se trouve dans un autre *reposiroty*, il faut préciser l'url. Par exemple: `git pull https://github.com/GauthLin/BeachBotEcam.git` pour récupérer les fichiers qui sont chez moi.


Si vous voulez *merger* vos modifications chez moi, il faut créer une *pull request*. Pour ce faire:

* Il faut aller sur votre *repository* du serveur
* Cliquer sur **pull request** qui se situe à droite
* Ensuite **New pull request**. 
* Pour finir, **Create pull request**

Là Github va vous lister toutes les différences entre vos fichiers et mes fichiers. S'il est marqué *Can be merged automatically* tout est bon ***sinon*** c'est qu'il y a conflit et là c'est pas bon ^^