## Que fait ce bot actuellemnent...?
- Un bot Discord spécifié dans de la _musique_, le but de ce projet est de pouvoir gérer la musique en plus de la faire jouer.

## Changelog:
* Ajout d'une __classe__ existante dans le `module Discord`:
    - FFmpegPCMAudio

* Ajout d'un `module`:
    - Youtube_DL

* Ajout de deux __commandes__:
    - resume
    - pause

## La conception du programme:
* V1:
    - Caractère d'exécution des commandes du bot : **-**.
    - Token appartenant à l'application Musicx.
    - Une fonction `join` pour rejoindre un salon vocal sur Discord.
    - Une fonction `quit` pour faire quitter d'un salon vocal.
    - Une fonction `stop` pour faire arrêter la musique en cours de lecture.
    - L'exécuton du programme avec le Token servant comme accès à __Musicx__.
* V2:
    - Une fonction `resume` pour recontinuer de jouer la musique.
    - Une fonction `pause` pour mettre en pause la musique.
* V3:
    - __FFMPEG__ pour que le salon vocal de Discord détecte la présence de `son` de la part de Musicx.
    - __Youtube_DL__ pour la recherche de musique sur YouTube.
    - Une fonction `play` pour jouer de la musique.
        + Musique joué depuis un _URL YouTube_.
    - Une fonction `clear` pour effacer les messages du salon textuel.