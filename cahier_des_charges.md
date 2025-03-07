# Cahier des charges !!!
Voici le cahier des charges pour le projet, Archero Zombie Mode !

Le but du jeu est que vous êtes une tourelle qui doit, par tous les moyens, esquiver les obstacles nommés Zombies. Vous pouvez vous déplacer dans la zone qui vous ait destinée, et qui sera aussi votre lieu de mort.
Le jeu utilise Les touches ZQSD.
Ce jeu est original car il offre de toutes nouvelles fonctionalités telles que bouger une tourelle, tout en esquivant les obstacles.
Il est aussi innovatif car il offre un mouvement plûtot fluide de la caméra, et ses différentes couleurs le rendent unique dans son genre.
Archero: Zombie Mode! est ainsi un bon jeu pour les débutants et avancés, où le but est de toujours battre son meilleur score!
Le jeu n'est pour le moment disponible que sur PC. A voir selon l'avancée.

Type de jeu: Arcade
Developpeurs: WILLIER Axel, 

## Objectifs
- Faire un interface séduisant
- Faire un menu pour pouvoir changer la difficulté
- Un système de récompenses
- Un gameplay addictif
- Un FPS résonnable
- Séduire le prof
- Obtenir le 20/20

## Contraintes

Il existe de plusieurs contraintes dans notre projet:
- Le travail de groupe sera un obstacle majeur dans notre projet, puisque nous ne sommes pas vraiment expérimenté dans la coordination de nos tâches et surtout que l'on en saît pas vraiment encore bien utiliser github et rendant ainsi la transmissions des informations un peu plus compliquées. (Merci David)
- L'optimisation du script, sachant que p5 est extrêmement nul à ce niveau. Garder un FPS qui reste jouable, une rapidité du jeu tout en améliorant les effets rendent cette contrainte d'une ampleur mesurable.
- Les maths restent aussi une épreuve importante dans notre projet puisqu'il est basé énormément sur l'orientation et les différentes positions du joueur. On pourrait aussi aborder le fait que les AI des zombies sont aussi compliquées à faire et demande un organisation plûtot importante.
- Sahcant que nous ne connaissons pas les goûts du prof, nous ne savons pas exactement par où commencer pour le séduire. Nous menant discrètement vers le 20/20. Cependant je doute qu'il note exclusivement sur la beauté du projet, ce qui revient aux contraintes supérieures.
- La détection de la collision est plûtot compliquée
- On utilise pas tous le même interpréteur. (Isaac)
- Les sauvegardes, qui sont un tout petit peu compliqués à exploiter sans script qui modularise le tout
- La structure du code, qui diffère selon le niveau, rend la fusion des scripts très compliqué lorsqu'on rassemble les travaux de chacun.
- Le FPS est très instable à cause du nombre de cercle et de dessins sur l'écran chaque secondes. C'est dommage que l'on ne peut pas exécuter les tâches en parralèles avec p5...

## Liens

Lien vers le Trello: https://trello.com/b/aWHJVvDJ/projet-n3-nsi-terminale-sam-alex-isaac
L'interpolation linéaire: https://fr.wikipedia.org/wiki/Interpolation_linéaire
Lien vers log1p, qui aurait pu être utilisé pour une croissance exponentielle de la fréquence des mobs en fonction du score du joueur: https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Math/log1p
Lien vers la documentation de sqllite3: https://www.sqlite.org

## Schémas

![image](https://github.com/user-attachments/assets/82a39611-9535-4ce3-81ae-9dec0ab30040)

*Schéma représentant l'angle d'orientation entre le joueur (Le point O) et la souris (le point P) grâce à la formule atan2(X,Y) où X = xO - xP et Y = yO - yP*

![image](https://github.com/user-attachments/assets/2b8577b3-afb7-4a5b-b984-b50f5ab5e998)
*Croquis de l'interface graphique de notre ancienne idée, Un Deminer spéciale.*

![Dessin du calcul de collisions pour le cercle](https://github.com/user-attachments/assets/3bea7350-9f70-4a83-a372-d9af34f71471)
*Croquis de l'obtention de la collision pour le joueur. Après de longues recherches.*

![Calcul de la vitesse d'apparition des mobs en fonction du temps et du score](https://github.com/user-attachments/assets/baaf6db4-7bd2-4590-88a9-56b51be7be78)
*Croquis de l'augmentation de la fréquence d'apparition des mobs en fonction du score du joueur*
