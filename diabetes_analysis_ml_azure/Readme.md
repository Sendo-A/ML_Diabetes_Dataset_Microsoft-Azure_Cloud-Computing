**FIELD : DATA ENGINEERING**

**PROJET CLOUD COMPUTING ON DIABETES DATASET**

**WITH MICROSOFT AZURE**

**Réalisé par : Abdelhadi CHAJIA**

![Cover image for Cloud Computing, Microsoft Azure](media/bb2729a95ae55d5763264fc1f5ab8e94.jpeg)

**L’objectif du projet est la mise en pratique des différentes notions étudiées dans ce module avec les outils et services offertes par Microsoft Azure, et les services de Machine Learning et de conteneurisation en local ou bien sur Cloud, et ce en utilisant un dataset simple (Pima Indian Diabetes Database) .**

1.  **Créer et Accéder à une Machine virtuelle Ubuntu sur le cloud Ms Azure**

**Suivre les étapes de création d’une machine virtuel sous azure**

**Remplir les champs nécessaire pour la création**

-   **Resource groupe**
-   **Le nom de la machine**
-   **Operating system**
-   **Mot de passe**
-   **Ssh log in**

![](media/2a5b534ee4a2678ec0b388376db528cd.png)

![](media/c9e926f36ca6f49e23968d0b85279b11.png)

**Choisir le type HDD car c’est moins cher**

![](media/8500c48eeddc2f664d3e2dca9addd2a9.png)

![](media/9891b702bbbdddd1890d4741f4f4ae2d.png)

![](media/fd29341ae640cf875501b2fbc7482be8.png)

**S’identifier à la machine virtuelle à l’aide du terminal linux avec le SSH installé**

**Ssh abdelhadi@20.25.131.3**

![](media/b5eaa79067c7507a3d32ca0bf3486c10.png)

1.  Attacher un disque HDD à cette machine, monter ce disque et déposer le dataset en question sur

ce disque attaché.

![](media/9626edf353f3381b76607c9f0494a6f6.png)

![](media/e9dd654c913b455aee5e5242b5e75b14.png)

![](media/603e3a1e19d6744a9ce120b6afc771e2.png)

![](media/92c64adf65c274d1aebbf4fe67e165b2.png)

![](media/f4363bc7bc763510956a6d3e65caf8e6.png)

![](media/d3c2a1516f8b866b26a83c167918d810.png)

1.  3\. En utilisant le Designer sur Azure ML services, explorer le dataset (types des variables, spécification de la variable Target, corrélations…)

![](media/0970253b61b8de0df2809f9c564362fd.png)

![](media/84099863638159d2a99ec20ff73f18f1.png)

![](media/f4caf84708195fa37b57f921b7a2f5a3.png)

![](media/120ef0130aa3871dd7af38c160e593e9.png)

![](media/c4affc986ba0d277f2fc9b8bc106352b.png)

![](media/ab5541416c20c365b2629dfe22274f63.png)

![](media/5c324cf20626c19d1441b612f309a14f.png)![](media/a2ebe8baa46303d82d96956b3c776b7b.png)

![](media/405e93ee0921dea9beee96c2ac5248d3.png)

1.  En utilisant le designer et à l’aide de l’algorithme de la régression logistique, créer un job pour

    entrainer et évaluer le modèle, afficher les résultats.

![](media/6568a6848b4f026b364a8f46927be3ea.png)

![](media/65f2c4c8ba74fff385cc5ac30acdaa76.png)

![](media/71e71f4b5b6f8fa3687149b3cece00bd.png)

![](media/3be59109030b8f2b72d020e55cd04539.png)

![](media/302f2a049b570ff86f9e509d63e194f0.png)

1.  En utilisant AutoML, déterminer le meilleur modèle, expliquer pourquoi

![](media/a7844a7b1dba6397a98ba3343bd4db58.png)

![](media/2d37ea45af45bf7a4cfb1c0ad539dfe3.png)

![](media/d49e57877b575b643f2e620bc06d8c6b.png)

![](media/d86a9384874db905b32441ee543908a0.png)

![](media/9a8bc6433110669d56428aa11ab0b093.png)

![](media/660cabbeb1658521b22b185545355bae.png)

![](media/8d9d478b0f24cbf321bf52ee372c45e8.png)

![](media/debb634335330fd440ec1dbe42028589.png)

![](media/b6ed4a7576df0b0a21dea31416e3035f.png)

![](media/128f497ce4123af4c8b1bf89455d90de.png)

![](media/dd29614396888f1f0bef4a41770d8592.png)

![](media/326df57b112a41d48c8b74ea01b53c19.png)

![](media/14a0741237ceadba92c91f1123e018d9.png)

![](media/003b2a29a9818dd35beff3e5cceef23f.png)

![](media/113b81ad82205a63e45aa3eebe21a207.png)

![](media/2cf5861eb42f9ca299f7e7f24dc940d4.png)

1.  Tester le modèle choisi avec des exemples.

![](media/95eee3f186fe1021e0afcbb44c55bddf.png)

![](media/f586d063b96d510c75e615e749a53e9b.png)

![](media/6c8606d400d04c52ccb99ffe6c0a36a9.png)

![](media/41e20b5c4760d287b061c1ee61509156.png)

![](media/41e20b5c4760d287b061c1ee61509156.png)

1.  Récupérer le code python et le fichier. pkl de ce modèle choisi .

    C’est fait voir le fichier joint

2.  Déployer le modèle sur Azure App services en utilisant GitHub, le fichier .pkl récupéré et

    streamlit ou bien flask.

![](media/e590104e1c26971ccc139ab6cf5c72e5.png)

![](media/a7daa947d33281cd86004ebde7e65f21.png)

![](media/f82e6933f426bb5e17e20898b03a0614.png)

![](media/3d644fd299f7ad0608b6b8f69fbd34c3.png)

![](media/556391b944c5d70f54048a343eebe094.png)

![](media/feaf075ae002bfdf007142692291e92e.png)

![](media/5c15b997f9c0aa11c71edbcd0f8272f2.png)

![](media/5425970216d4cb86939996684baba4e4.png)

![](media/88608d44458bde22239507aec8606aa7.png)

![](media/fe6bcad9ee26be2d3abc981ba6442d81.png)

![](media/d018804267d0bb819c68e92c8dd6741f.png)

![](media/b7d0c9b4d2a55968cc538f5548f3cd96.png)

![](media/9a0dafe369b2dd132f2d08c45b664a67.png)

![](media/a809ac4aaa4bfd3eced4aee27bb4ffe1.png)

1.  Utiliser Application Gateway pour Sécuriser App service et la VM (autoriser l’accès à votre

    adresse ip seulement pour ces deux ressources).

![](media/d12683e811fe5e704eb4578d4493c83d.png)

![](media/5b13d3a86da657bfc1a4ea071f041a52.png) ![](media/38b53673ef15850b436c4ee257345e9e.png)

![](media/60c70acf0d1700afa38b7be1c43ca87d.png)

![](media/148571712ad1f78baabee1eef16bc609.png)

![](media/d9d2b3d58795dcaaef481e344f604b33.png)

![](media/ec090135b3cb647b31b467e60f120240.png)

![](media/b7938ca57a56cdbd3dd1d62da179994c.png)

![](media/c4ff6cf30524eae9cf2507b52064f096.png)

![](media/0edb866f0caafc26aca8340065efc293.png)

![](media/da737fe39ab9087140fc69012efed48f.png)

![](media/cf0d8e7929bb8f72244053154ea6a0be.png)

1.  En local, créer une image conteneurisée depuis l’application web déployé et lancer un conteneur

![](media/7d5db8d00b0496c891cd750a46ffd147.png)

![](media/2ccf3e949a2be8c663aa206b431ff8f9.png)

1.  Déployer l’image sur Azure Kubernetes Service (AKS).

![](media/4e098ccfce0b268cecf3860dbbeeead9.png)

![](media/d471ca76f86367ccfdfc3a8ddfc7419e.png)

![](media/e8ebe4f78654752accef4fa3b39d283c.png)

![](media/4aaaedbe2f4d2a11a9bed2b1b49a2789.png)

![](media/025a405411e2078802d87489228b55c6.png)

![](media/274e089ab1f1dacb89b3c135f503da07.png)

![](media/321404289946f888538a63102ba4198a.png)

![](media/1820787aa10a7f48aa72bf7ff483c2f0.png)

![](media/0811c23bea1282d10c6633e19849b7fd.png)

![](media/09614a49680be3164c1974586a9946b1.png)

![](media/cab154d3a1641f0b623825840c29fa1c.png)

![](media/fe93463f3f95bd3f8c94496bcb60e8e6.png)

![](media/8b4e3ddcbee0d1b407cfe1bea66c0825.png)

![](media/62f522b661c393e5367fc9323c05b3d9.png)

![](media/798064f82d0e4988408b45d0f7bc0c19.png)

![](media/a79225c296ce76436d84f99ac1550702.png)

![](media/3b502ec48dfbeb79dda64eed1357cdf1.png)

![](media/79c562826cbf11775a67199654c9cdd3.png)

1.  12\. En utilisant le code python récupéré, créer un notebook sur Azure Databricks et entrainer le dataset avec le modèle choisi.

![](media/b876a145f214e2fb6f483c898fd03e56.png)

Le notebook est en fichier joint

FIN
