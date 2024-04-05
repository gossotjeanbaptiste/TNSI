# Tout ce qu'on a vu sur la cryptographie:

- Chiffrement symétrique : 
  * Même clé
  * Même algorithme
  
- Vulnérabilités : 
  * Attaque par force brute
  * Par leur problème mathématiques
  * Eviter les interceptions (Man in the middle)
  
- Contrainte : 
  * La clé doit être communiquée de manière sécurisée
    Exemple : 
    * Se voir en vrai
    * Passer par une info privée que seuls qui communiquent connaissent
  
Le chiffrement symétrique à un talon d'achille et on doit imaginer une autre solution pour se transmettre les clés. 

### Conclusion : 
- On se sert d'une autre méthode de chiffrement pour partager notre clé de chiffrement symétrique.
- Une solution a été proposé par Diffie et Hellman en 1976. (Méthode Diffie-Hellman)

Par convention, en cryptographie c'est Alice qui envoie un message à Bob. Et le pirate est Charlie qui écoute la conversation. 
