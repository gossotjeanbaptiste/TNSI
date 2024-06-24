# Préambule/Prérequis

- Avoir un compte GitHub
- Avoir Git Bash installé sur votre machine

---

## Comment avoir une clé SSH et comment la mettre sur GitHub

---

### 1. Générer une clé SSH

1. Ouvrez Git Bash
2. Tapez la commande en 2.1 ou 2.2
- 1. `ssh-keygen -t ed25519 -C "your_email@example.com"`
- 2. `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
3. Appuyez sur `Entrée` pour accepter le chemin par défaut
4. Entrez un mot de passe sécurisé (optionnel) et retapez-le pour confirmer (si vide alors appuyez deux fois sur `Entrée`)
5. Vous avez généré une clé SSH

---

### 2. Ajouter la clé SSH à l'agent SSH

1. Dans La Windows POWERSHELL ADMINSTRATEUR taper cette commande `Get-Service -Name ssh-agent | Set-Service -StartupType Manual`
2. Faite `Start-Service ssh-agent`
3. Ajoutez votre clé SSH à l'agent SSH en tapant la commande `ssh-add ~/.ssh/id_ed25519` ou `ssh-add ~/.ssh/id_rsa` (Selon si vous avez choisi l'option 2.1 ou 2.2 du point 1)

---

### 3. Ajouter la clé SSH à votre compte GitHub

1. Copiez la clé SSH dans le presse-papiers en tapant la commande `clip < ~/.ssh/id_ed25519.pub` ou `clip < ~/.ssh/id_rsa.pub` (Selon si vous avez choisi l'option 2.1 ou 2.2 du point 1)
2. Allez sur GitHub
3. Cliquez sur votre photo de profil en haut à droite
4. Cliquez sur `Settings`
5. Cliquez sur `SSH and GPG keys`
6. Cliquez sur `New SSH key`
7. Collez la clé SSH dans le champ `Key`
8. Cliquez sur `Add SSH key`
9. Entrez votre mot de passe GitHub
10. Vous avez ajouté la clé SSH à votre compte GitHub

---

### 4. Tester la connexion SSH

1. Tapez la commande `ssh -T git@github.com`
2. Tapez `yes` puis appuyez sur `Entrée`
3. Vous devriez voir `Hi <your_username>! You've successfully authenticated, but GitHub does not provide shell access.` `<your_username>` étant votre nom d'utilisateur GitHub
4. Vous avez testé la connexion SSH

---

### 5. Utiliser la connexion SSH

1. Allez sur un dépôt GitHub
2. Cliquez sur `Code`
3. Cliquez sur `SSH` et copiez le lien
4. Ouvrez Git Bash
5. Tapez la commande `git clone <lien_ssh>` (remplacez `<lien_ssh>` par le lien copié)
6. Vous avez cloné un dépôt GitHub en utilisant la connexion SSH
