# Portefeuille Norvège ONU Femmes RDC

Site public de visibilité documentaire consacré au partenariat Norvège–ONU Femmes et aux institutions et organisations partenaires en RDC. Version préparée le 8 octobre 2026, à partir des sept fichiers transmis. Le site ne se présente pas comme un domaine institutionnel officiel.

## Consulter localement

Ouvrir `index.html` dans un navigateur. Aucun serveur, compte, clé API, service externe ou installation n’est nécessaire. Les données et la carte sont embarquées localement. Les publications publiques s’ouvrent sur le site d’ONU Femmes.

## Contenu

- Présentation des phases 2022–2024 et novembre 2024–décembre 2027.
- Douze indicateurs avec filtres, source et note de périmètre.
- Carte des 26 provinces, cinq provinces cliquables et sélecteur accessible.
- Seize fiches partenaires harmonisées représentant 22 accords.
- Recherche par nom ou initiative et filtres territoire/type.
- Détail des accords et export CSV protégé contre les formules de tableur.
- Récits illustrés avec photographies issues des rapports.
- Registre des sept documents et méthode de lecture.

## Déploiement prévu

Dépôt recommandé : `globalgreenwaybusiness/portefeuille-norvege-onufemmes-rdc`.

1. Créer ce dépôt public (le code et les contenus publics seront visibles).
2. Déposer tous les fichiers de ce dossier à la racine, y compris `.github/workflows/pages.yml` et `.nojekyll`, sur la branche `main`.
3. Dans **Settings > Pages > Build and deployment**, sélectionner **GitHub Actions** comme source.
4. Dans **Actions**, lancer « Publier le portefeuille sur GitHub Pages » si la première exécution précède l’activation de Pages.
5. Vérifier le succès des jobs `build` et `deploy`. L’adresse du site sera celle renvoyée par le job de déploiement.

Adresse attendue après un déploiement réussi : `https://globalgreenwaybusiness.github.io/portefeuille-norvege-onufemmes-rdc/`.
Cette adresse est une destination prévue, pas une confirmation de publication.

Documentation : https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Mettre à jour les données

Modifier `data/portfolio.json`, puis régénérer sa version navigateur :

```bash
python3 scripts/sync_data.py
python3 scripts/validate.py
node --check app.js
```

Les fiches utilisent une clé stable `partner`. Chaque accord conserve son code source. Les périodes contractuelles ne sont pas présentées comme un statut d’achèvement. Le fichier `portfolio.js` est une copie navigateur du JSON pour permettre l’ouverture locale sans serveur.

La carte conserve le GeoJSON d’origine et utilise `data/map.js` pour afficher des chemins SVG préprojetés. Lors d’un changement de fond, régénérer `data/map.js` avec `python3 scripts/sync_data.py`.

## Règles éditoriales

Les montants des programmes en NOK, les valeurs contractuelles en USD et les dépenses sont distincts. Ne pas convertir les devises sans taux daté. Les accords cofinancés ne sont pas attribués intégralement à la Norvège. Ne pas sommer les participations pour obtenir des bénéficiaires uniques. Les dates limites de couverture des rapports sont signalées dans le site.

Les rapports originaux ne sont pas distribués. Aucun nom de gestionnaire d’accord, contact personnel ou détail individuel de protection n’est inclus. Les photographies sont reprises des documents fournis et leurs droits demeurent auprès de leurs titulaires. Ne pas ajouter de données personnelles au dépôt public.

## Vérifications réalisées

Contrôle syntaxique JavaScript et validation des données, totaux par attribution, correspondance JSON/JS, ressources locales, liens internes et sources. Tests d’interaction DOM sur les filtres, recherche, carte, fenêtres de détail et export. La vérification visuelle dans un navigateur reste à effectuer avant validation finale de la présentation.

## Crédits

Voir `SOURCES.md`. Les mentions institutionnelles en en-tête sont typographiques ; aucune identité officielle ou logo institutionnel n’a été reconstitué.
