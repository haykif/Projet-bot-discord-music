## Que fait ce bot actuellemnent...?
- Un bot Discord spécifié dans de la _musique_, le but de ce projet est de pouvoir gérer la musique en plus de la faire jouer.

## Changelog:
- Modification intégrale du code python du bot en question.
- Changement du __Token__ pour la raison de son expiration avec sa mauvaise utilisation.
- téléchargement de `PyNaCl`:
    * PyNaCl est une liaison Python à `libsodium`. Ces bibliothèques ont pour objectif déclaré d’améliorer la convivialité, la sécurité et la vitesse.
- Choix du design du __logo__ et du __nom__ du bot qui est de `Musicx`.
- Sur Discord: Mise à jour sur l'activité du bot avec un petit message s'afichant à côté du petit voyant vert 🟢 indiquant qu'il est bien en ligne: `Écoute DR.Dre Still`.

## La conception du programme:
* V1:
    - Caractère d'exécution des commandes du bot : **-**.
    - Token appartenant à l'application Musicx.
    - Une fonction `join` pour rejoindre un salon vocal sur Discord.
    - Une fonction `quit` pour faire quitter d'un salon vocal.
    - Une fonction `stop` pour faire arrêter la musique en cours de lecture.
    - L'exécuton du programme avec le Token servant comme accès à __Musicx__.