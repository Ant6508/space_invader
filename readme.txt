Space Invaders

Ce jeu dispose de 10 niveaux débloquables les uns après les autres à difficultées croissantes.
Dans le menu, le joueur peut soit sélectionner un niveau grace aux 10 boutons pour refaire un niveau qu'il a déjà fait ou  appuyer sur jouer pour lancer le dernier niveau qu'il n'a pas débloqué.

le jeu possède plusieurs types d'aliens différents ayant des fonctionnalités singulières ( suivre le joueur , tirer ... ) qui apparaissent au fur et à mesure .

Le joueur gagne des points en éliminant les aliens mais attention à ne pas se retrouver à cours de vies ... 

CHEAT CODE
En appuyant sur la touche c , une fenêtre s'ouvre et le joueur peut rapidement entrer l'un de ces cheat code :
- END : fini le niveau en cours et débloque tous les autres ( tous les aliens de la vague courante soivent avoir spawnés ! )
-superman : le joueur devient invincible
-CPE4LIFE : donne 1000 vies au joueur

BONUS :
Le joueur peut en jeu ramasser différents bonus qui l'aideront à vaincre les aliens
- en augmentant la vitesse de tir du joueur
- en lui donnant une vie supplémentaire
- en le rendant invincible pendant un cours laps de temps

De plus, lorsque le joueur perd une vie, il devient de même invincible pendant 2 secondes


Je n'ai pas eu le temps de créer tous les niveaux que je voulais à cause du code qui devenait difficile à débugger ( par exemple le boss qui devient invisible n'est pas concerné par les collisions )
Cependant, comme toutes les classes sont crées, il suffit de se rendre dans le module niveau_classes et ajouter les aliens dans la liste aliens_waves

Cette liste est surement la plus importante du code ( même si c'est loin d'être la seule ) : elle indique au jeu les aliens qui doivent spawn sous forme de différentes vagues.
Les aliens sont ainsi totalement modifiables au niveau de leur stats mais aussi au niveau de leur fonction de déplacement.

Juste avant qu'un alien spawn, python va regarder dans le ficher aliens_classes si une ou plusieurs fonctions de deplacement ont été créees
( on a juste besoin d'une seule fonction de déplacement par type d'alien car si aucune fonction de deplacement n'est déclarée pour la vague k c'est
la fonction de déplacement de la vague 0 qui va lui être attribuée ) .

Pygame n'est utilisée que pour la musique

Enfin, il est possible de faire apparaître la hitbox des différents éléments du canvas (aliens,missiles,vaisseau) en appelant la fonction display_bbox à l'initilisation de la classe
correspondante ) ainsi que le nombre d'entités présentes sur le canvas en appuyant sur la touche "d".