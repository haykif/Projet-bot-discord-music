# PyNaCl
- Le premier problème que j'ai eu, c'était avec la liaison `PyNaCl`. Mon code Python de mon bot Discord ne voulait pas s'exécuter et affichait comme erreur __PyNaCl was not Found__.
    * C'est grâce à mon camarade de classe `Gaëtan` que j'ai réussit à le résoudre, il m'avait dit d'installer PyNaCl depuis un terminal dans système avec la commande _pip3_.

# -play
- Le second probleme que j'ai rencontré, c'est avec ma commande `-play`. Dans cette commande nous avons une fonction _play_ qui installe la musique recherché avec un URL sur YouTube grâce à `Youtube_DL`, mais le seul bémol c'est qu'il ne jouait pas la musique installée. L'erreur était avec le micro-logiciel émmettant le son installé dans un salon vocal, étant __FFMPEG__ (faisant en sorte que la musique soit émis comme si une personne parlait dans son micro, dans le salon vocal).
    * J'ai réussi à résoudre se problème en visonnant des vidéos sur YouTube et en lisant/regardant les forums sur ce sujet. Le problème était logique, je n'avais pas précisé que __FFMPEG__ devait se connecter aussi au salon vocal de l'utilisateur exécutant la commande.