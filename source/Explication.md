# Explications

## Travail effectué

***Pour chaque fichier .cs (qui sont ceux dans lesquels nous avons codé), le code source est répertorié sur le dépôt GitHub du projet. [Code source du projet OC_projet_Akim_Louis](https://github.com/AkimBerreqia/OC-projet-Akim-Louis/tree/main/OC_projet_Akim_Louis/Assets/Script)***

### Akim

Je me suis occupé de faire les attaques du joueur, ainsi que le système de menus (pour changer de niveau, pour mettre le jeu en pause, pour accéder aux différents types de projectiles). J'ai également produit le système de santé du joueur et des ennemis et le système de mana du joueur.
#### fichiers
##### 1. WinGame.cs:
Ce fichier contrôle si le joueur rentre en collision avec le "Roasty Meat". Si c'est le cas, alors la méthode "Win()" se lance et affiche le menu de victoire.
##### 2. UnlockBlockingPlatforms.cs:
Quant à ce fichier, il contient l'integer "lockers", qui est égal à l'integer "lockers" du fichier Blocker.cs pour chaque update.
##### 3. StartGame.cs:
Ce fichier est utilisé pour le Home Menu. Il contient trois méthodes. La première,"ChooseLevel()", est utilisée quand le button "CHOOSE LEVEL" est enclenché. Cela cache la fenêtre d'accueil pour montrer la fenêtre de choix de niveau.

La deuxième méthode, "Back()", fait l'action inverse de "ChooseLevel()".

Et pour la dernière méthode, "QuitGame()", elle ferme l'application. 
##### 4. Shot.cs:
Dans ce fichier, il y a des variables publiques pour le projectile lié au script et le mouvement du joueur, puisque la direction du joueur influence le point de départ du projectile. En général, le script s'occupe d'ordonner les actions de chaque projectile (déplacement et possède le script pour attaquer un ennemi).

Si le projectile est rouge et qu'il touche un ennemi, alors le booléen "isFired" est vrai. Ce booléen provient du script de l'ennemi touché, afin qu'il continue de subir des dégâts sur la durée. Sinon l'ennemi touché prend qu'une seul fois les dégâts du projectile.

Suivant le type de projectile, le projectile est visible ou non. Par exemple les projectiles vert sont des bonus au joueur, donc ils sont invisibles, puisqu'ils ne servent pas à attaquer.

Si le projectile est vert, alors le prochain a un bonus sur sa vitesse de déplacement et ses dégâts.
##### 5. SetHealth.cs:
Ce fichier la méthode "TakeDamage()" contient prend en paramètres : le nombre de dégâts infligés, le temps pour lequel le GameObject ne peut pas prendre de dégâts, sa santé actuelle, sa santé maximale, des informations sur la tailles de la barre de vie, et les dégâts initiaux.

Le GameObject va subir des dégâts à condition qu'il n'est plus invincible (le délai pour lequel il ne peut pas prendre de dégâts est terminé). La méthode retourne au GameObject son état de santé, ses dégâts initiaux et la nouvelle taille de sa barre de vie.

Ensuite, il y a la méthode "GainHealth()", qui fonctionne similairement à la méthode précédente, mais pour que le joueur puisse gagner de la santé. La seul différence est que si la santé actuelle est au max, alors le joueur ne peut pas gagner plus de santé.
##### 6. Projectile.cs
Le fichier fait référence à plusieurs scripts pour vérifier les conditions suivantes.

Avec la méthode "InstantiateProjectile()", le projectile à instancier doit vérifier que le temps d'apparition entre lui et le projectile précédemment instancié est respecté, sinon le joueur pourrait tirer trop de projectiles en un espace de temps très court. Il est également vérifié que le joueur a suffisamment de mana pour tirer instancier le projectile. Ensuite, il faut vérifier la direction par laquelle le projectile doit partir, en vérifiant la direction actuelle de tire du joueur.

Enfin la méthode "Update()" contrôle que le joueur est vivant et que le jeu n'est pas en pause pour commencer la procédure d'"InstantiateProjectile()".
##### 7. Power.cs
Tout d'abord, un namespace est appelé pour utilisé une "RawImage", contenu sur le canva de chaque scène des niveaux. 

```C#
using UnityEngine.UI;
```

De cette façon la "RawImage" est appelé avec d'autres GameObjects qui gèrent l'interface des menus des projectiles. Il y a également deux scripts qui sont appelés.

```C#
public GameOverAndPauseMenu gameOverAndPauseMenu;
public PlayerHealth playerHealth;

public GameObject SpellsMenu;

public GameObject BasicSpellsTitle;
public GameObject BasicSpellsText;

public GameObject ComplexSpellsTitle;
public GameObject ComplexSpellsText;

public GameObject OpenBasicSpellsMenu;
public GameObject CloseBasicSpellsMenu;

public GameObject OpenComplexSpellsMenu;
public GameObject CloseComplexSpellsMenu;

public RawImage Arm;
```

Il y a par la suite chaque type de projectile qui est détaillé, avec sa couleur, son coût en mana, son nombre de dégâts, sa vitesse, les dégâts qu'inflige l'ennemi touché et la vitesse de l'ennemi touché.

```C#
// private string[] states = {keyboardAssignment, color, manaCost, damage, speed, ennemyDamage, ennemySpeed};
private object[,] basicStatesArray = {
    { "1", Color.gray, 0f, 20f, 1f, 1f, 1f }, // neutral
    { "2", Color.red, -20f, 20f, 1f, 1f, 1f }, // fire
    { "3", Color.blue, -20f, 20f, 1f, .5f, .5f }, // water
    { "4", Color.yellow, -20f, 40f, 1.5f, 1f, 1f }, // lightning
    { "5", Color.green, -20f, 0f, 0f, 0f, 1f } // wind
};


private object[,] complexStatesArray = {
    { "1", Color.black, -30f, 50f, .5f, 1f, 1f }, // shadow
    { "2", Color.white, -30f, 20f, 4f, 1f, 1f } // light
};
```

Il y a différentes variables qui sont appelées pour la couleur de base du "Arm Icon" et le reste se concentre sur les statistiques du type de projectile qui est choisi par la joueur.

```C#
public Color CurrentColor = Color.gray;
public float currentManaCost = 0;
public float currentDamage = 20f;
public float speedMultiplicator = 1f;
public float ennemyDamageMultiplicator = 1f;
public float ennemySpeedMultiplicator = 1f;
public float fireDamage;

public bool spellIsBuffed = false;
private bool isAlted = false;
private bool isTabed = false;
```

Ensuite il y a la méthode "ChangeElement()" qui change la couleur de l'indicateur du type de projectile équipé dans l'HUD (Heads-Up Display / affichage qui renseigne le joueur sur certains de ses attributs) du joueur.

```C#
public void ChangeElement(RawImage Arm, Color color)
    {
        Arm.color = color;
    }
```

Puis, la méthode public "FindElement()" va attribuer aux variables précédemment mentionnées les informations liées au projectile choisi par le joueur.

```C#
// Update current stuff
void FindElement(object[,] statesArray)
{
    for (int i = 0; i < statesArray.GetLength(0); i++)
    {
        if (Input.GetKeyDown(statesArray[i, 0].ToString()))
        {
            CurrentColor = (Color)statesArray[i, 1];
            currentManaCost = (float)statesArray[i, 2];
            currentDamage = (float)statesArray[i, 3];

            if (i == 1)
            {
                fireDamage = currentDamage;
            }

            speedMultiplicator = (float)statesArray[i, 4];
            ennemyDamageMultiplicator = (float)statesArray[i, 5];
            ennemySpeedMultiplicator = (float)statesArray[i, 6];

            ChangeElement(Arm, CurrentColor);
        }
    }
}
```

Il faut en premier lieu trouvé quel type de projectile est choisi par le joueur, puis il faut attribuer les valeurs du type choisi pour les prochains projectiles à instancier.

Pour la méthode "Start()", chaque fois que la scène contenant le fichier démarre, la couleur de base de l'indicateur du type de projectile équipé retourne sur le normal (couleur gris). L'HUD des menus des projectiles et remis à défaut.

```C#
// Start is called before the first frame update
void Start()
{
    Arm.color = Color.gray;

    SpellsMenu.SetActive(false);

    BasicSpellsTitle.SetActive(false);
    BasicSpellsText.SetActive(false);

    ComplexSpellsTitle.SetActive(false);
    ComplexSpellsText.SetActive(false);

    OpenBasicSpellsMenu.SetActive(true);
    CloseBasicSpellsMenu.SetActive(false);

    OpenComplexSpellsMenu.SetActive(false);
    CloseComplexSpellsMenu.SetActive(false);
}
```

Enfin, la méthode "Update()" va cacher l'HUD des projectiles si le jeu est en pause ou que le joueur est mort. La méthode va également gérer tout le système de cet HUD, en changeant les menus affichés selon les actions du joueur.

```C#
// Update is called once per frame
void Update()
{
    if (gameOverAndPauseMenu.isPaused == false && playerHealth.isAlive == true)
    {
        // If basic spells menu is closed when you click on "Tab",
        // it initializes the bools for the basic and complex spells menus
        if (Input.GetKeyDown(KeyCode.Tab) && isTabed == false)
        {
            isTabed = true;
            isAlted = false;
        }

        // If basic spells menu is opened and complex spells menu is closed,
        // the complex spells menu can be opened
        else if (Input.GetKeyDown(KeyCode.LeftAlt) && isTabed == true && isAlted == false)
        {
            isAlted = true;
        }

        // If basic and complex spells menus are opened when you click on "LeftAlt",
        // the complex spells menu can be closed and then can return back on the basic one
        else if (Input.GetKeyDown(KeyCode.LeftAlt) && isTabed == true && isAlted == true)
        {
            isAlted = false;
        }

        // If any of the menus are opened when you click on "Tab",
        // every menus can be closed
        else if (Input.GetKeyDown(KeyCode.Tab) && isTabed == true)
        { 
            isTabed = false;
            isAlted = false;
        }

        // It opens the complex spells menu
        if (isAlted == true)
        {
            FindElement(complexStatesArray);

            BasicSpellsTitle.SetActive(false);
            BasicSpellsText.SetActive(false);

            ComplexSpellsTitle.SetActive(true);
            ComplexSpellsText.SetActive(true);

            OpenBasicSpellsMenu.SetActive(false);
            CloseBasicSpellsMenu.SetActive(true);

            OpenComplexSpellsMenu.SetActive(false);
            CloseComplexSpellsMenu.SetActive(true);
        }

        // It opens the basic spells menu
        else if (isTabed == true)
        {
            FindElement(basicStatesArray);

            SpellsMenu.SetActive(true);

            BasicSpellsTitle.SetActive(true);
            BasicSpellsText.SetActive(true);

            ComplexSpellsTitle.SetActive(false);
            ComplexSpellsText.SetActive(false);

            OpenBasicSpellsMenu.SetActive(false);
            CloseBasicSpellsMenu.SetActive(true);

            OpenComplexSpellsMenu.SetActive(true);
            CloseComplexSpellsMenu.SetActive(false);
        }

        // It closes every spells menus
        else
        {
            SpellsMenu.SetActive(false);

            BasicSpellsTitle.SetActive(false);
            BasicSpellsText.SetActive(false);

            ComplexSpellsTitle.SetActive(false);
            ComplexSpellsText.SetActive(false);

            OpenBasicSpellsMenu.SetActive(true);
            CloseBasicSpellsMenu.SetActive(false);

            OpenComplexSpellsMenu.SetActive(false);
            CloseComplexSpellsMenu.SetActive(false);
        }
    }
}
```
##### 8. PlayerHealth.cs
La méthode "PlayerRecovers()" va mettre à jour les données de santé du joueur en se servant de la méthode "GainHealth()" du script "SetHealth".

"PlayerLoosesHealth()" fait perdre de la vie au joueur et est enclenché lorsque la méthode "OnTriggerStay2D()" détecte une collision entre un ennemi et le joueur, alors qu'il est toujours vivant.

La méthode "Die()" change la couleur du joueur pour signaler qu'il est mort. Le joueur ne peut plus bouger lorsqu'il meurt.

La méthode "GameOver()" va faire appelle à la méthode "Die()", puis va cacher tout l'HUD et n'importe quel autre menu qui pourrait être présent à l'écran pour afficher à la place de menu de GameOver.

La méthode "Start" va donner le nombre maximum de santé au joueur, ainsi qu'un masse de 20 unités. Les menus pause, de GameOver et de victoire sont cachés.

Dans la méthode "Update()", le script contrôle si le joueur a perdu tous ces points de santé. Si c'est le cas, alors il fait appelle à la méthode "GameOver()".

Pour la méthode "OnTriggerEnter2D()", le joueur meurt s'il rentre en contact avec la zone de mort.
##### 9. MedicalKitNumber.cs
Ce script permet d'actualiser le nombre de "Medical Kits" en possession du joueur, en l'indiquant dans l'HUD du joueur.

Au départ le joueur commence avec zéro "Medical Kits", puis s'il entre dans la zone de "Trigger" d'un "Medical Kit", alors ce dernier disparaît pour augmenter de un la quantité possédé par le joueur. Cela fonctionne si le joueur n'a pas sa quantité maximale de "Medical Kits" atteinte. Dans ce cas,  il ne se passe rien.

Si à la place, le joueur entre dans la zone de "Trigger" d'un "Medical Kit Shelf", alors un texte apparait à l'écran pour signaler que le joueur peut remplir sa quantité de "Medical Kits" au maximum.

Sinon, le joueur peut appuyer sur la touche "H" du clavier pour consommer un "Medical Kit", à condition que sa santé ne soit pas au maximum, et que le joueur contienne au moins un "Medical Kit".
##### 10. Mana.cs
Le script s'occupe de gérer le niveau de mana, qui est plein quand la scène est chargée. Si le joueur tire un projectile, alors son niveau de mana diminue. Ceci peut aller jusqu'à que son niveau de mana soit à zéro.

Puis si le joueur ne relance pas de projectile, alors son niveau de mana remonte petit-à-petit. Il y a également un temps pour lequel le mana ne peut pas remonter tout de suite, ou diminuer (ce qui limite le nombre de tirs).

La mana fonctionne de façon assez analogique à la santé, pour les méthodes "SetMana()" et "RecoverMana()".
##### 11. ItemsMovement.cs
Ce script permet de rajouter du dynamisme à certains objets statiques ("Roasty Meat" et "Medical Kits"). Ils suivent un mouvement de montée et de descente en continu.
##### 12. GameOverAndPauseMenu.cs
Le script s'occupe de recharger la scène à son premier chargement. Il y a aussi une méthode qui renvoie au "Home Menu". Une autre méthode s'occupe de mettre en pause le jeu, en arrêtant le mouvement des ennemis et du joueur, tout en cachant l'HUD et en empêchant le joueur d'interagir.
##### 13. EnterBlockingPlatform.cs
Lorsque le joueur entre en "Trigger" collision avec la zone de "Trigger" qui se rapporte au GameObject lié à ce script, alors une platforme apparaît pour bloquer la suite du chemin.

Cette platforme qui bloque le chemin est de base inactive.
##### 14. Enemy.cs
Le script contient une méthode pour que l'ennemi qui est lié à ce script prenne des dégâts. Cette méthode est utilisée dans le script "Shot()".

Dans la méthode "Update()", il est vérifié si l'ennemi a été attaqué par un projectile de feu (couleur rouge). Si c'est le cas, la méthode "EnemyGetsDamaged()" doit être appliquée.

L'ennemi meurt s'il perd toute sa santé. Il ne peut plus bouger. Alors le GameObject de cet ennemi est détruit.

Ce script contient des informations qui sont seulement présente dans le niveau deux, car il y a un passage où une platforme empêche le joueur d'avancer, il doit donc tuer un ennemi pour que la platforme disparaisse. Une fois l'ennemi tué, il réduit de un l'integer "lockers" du script Blocker.cs, si ce nombre est plus grand que zéro, car il faut vérifier que le joueur n'a pas tué d'ennemi. Il se peut que l'ennemi meurt avant que la platforme apparaisse. c'est pourquoi il faut que le nombre "lockers" soit présent.

Si l'ennemi est un Boss, alors il doit mourir en faisant disparaître sa barre de vie, qui est présente dans l'HUD du joueur.

Le Boss apparaît après que le joueur à tué tous les ennemis de la zone. Il apparaît ainsi, en faisant aussi apparaître se barre de vie dans l'HUD du joueur, et non au dessus de lui.

Dans le niveau deux, le Boss rend inactif des "Jump Pads" qui permettent d'atteindre la fin du niveau. Mais une fois mort, les "Jump Pads" sont actifs.
##### 15. BossEmergence.cs
Le script s'occupe de rendre inactif le Boss et sa barre de vie, puisqu'il doit apparaître une fois que les ennemis de sa zone soit tous morts.

L'"Update()" vérifie quand les ennemis de la zone sont morts. Si cette condition est respectée, alors le Boss et sa barre de vie apparaissent.

Si le menu pause est activé, alors la barre de vie du Boss doit être inactive.
##### 16. BuildScene.cs
##### 17. Blocker.cs

### Louis

Je me suis occupé du mouvement du joueur et des ennemis ainsi que de la construction des niveaux (différents types de platformes -> de base, qui tombe ou qui bloque temporairement l'accès à la suite du niveau).
#### fichiers
##### 1. CameraFollow.cs
##### 2. FallingPlatform.cs
##### 3. JumpPad.cs
##### 4. Patrol.cs
```C#
public class Patrol : MonoBehaviour
{
    public Power power;
    public Enemy enemy;

    public float speed;

    private bool movingRight = true;

    public Transform groundDetection;

    void Update()
    {
        if (enemy.canMove == true)
        {
            transform.Translate(Vector2.right * speed * power.ennemySpeedMultiplicator * Time.deltaTime);
        }

        RaycastHit2D groundInfo = Physics2D.Raycast(groundDetection.position, Vector2.down, 2f);


        if(groundInfo.collider == false)
        {
            if(movingRight == true)
            {
                transform.eulerAngles = new Vector3(0,-180,0);
                movingRight = false;
            } else {
                transform.eulerAngles = new Vector3(0,0,0);
                movingRight = true;
            }
            
        }
    }
}
``` 
Ce fichier permet de faire patrouiller un ennemi sur une platforme.

Il est diviser en 3 parties:
    
    
    1. Appelation des variables
    2. Mouvement de l'ennemi
    3. Informations nécessaire pour le mouvement 

La première partie contient toute les informations nécessaire au bon fonctionnement du code. Les deux premières lignes permettent de customiser notre ennemi grâce au code fait par Akim, ensuite nous pouvons customiser la vitesse de l'ennemi et la direction dans laquelle il va se diriger au lancement du jeu. Le public Transform nous permet de référencer un élément accrocher à notre ennemi. 
```C#
public class Patrol : MonoBehaviour
{
    public Power power;
    public Enemy enemy;
----------- 1
    public float speed;
    private bool movingRight = true;
----------- 2
    public Transform groundDetection;
----------- 3
``` 

Ensuite, cette partie permet de faire bouger l'ennemi sur la platforme. 
```C#
if (enemy.canMove == true)
    {
        transform.Translate(|Vector2.right |* speed *| power.ennemySpeedMultiplicator *| Time.deltaTime);
    }
```
Il y a plusieurs éléments importants dans cette ligne. 

En premier, "transform.Translate" fait bouger l'ennemi "transform" dans la direction donnée par la fonction "Translate". 

Translate a plusieurs éléments utiles. Le premier "Vector2.right" créer un vecteur (0 1) pour faire bouger l'ennemi vers la droite. 

Ensuite, nous pouvons ajuster la vitesse avec laquelle il bouge grâce à "speed" qui était déjà défini avant. 

"Time.deltaTime" permet à la patrouille de mouver à vitesse constante. En effet, "Time" fait bouger l'ennemi à chaque frame, ce qui pourrait poser problème si le jeu tourne à 200 fps. En effet, comme le nombre de frames est plus grand, l'ennemi marcherait plus vite. Donc, nous utilisons "deltaTime" pour rendre "Time" constant, ce qui rend la vitesse de l'ennemi constante peu importe le nombre de fps. 

La dernière partie du code permet de regarder si l'ennemi est toujours sur la platforme et sinon le faire marcher dans l'autre sens.
```C#
RaycastHit2D groundInfo = Physics2D.Raycast(groundDetection.position, Vector2.down, 2f);
------- 1
if(groundInfo.collider == false)
------- 2
{
    if(movingRight == true)
    {
        transform.eulerAngles = new Vector3(0,-180,0);
        movingRight = false;
    } else {
        transform.eulerAngles = new Vector3(0,0,0);
        movingRight = true;
    }   
------- 3
}
```
Pour la première partie, nous envoyons un "Raycast" pour savoir si l'ennemi arrive vers le vide ou non. "groundInfo" est un bool qui va retourner "true" tant que le "Raycast" détecte quelque chose.

Ensuite, nous envoyons ce "Raycast", qui peut être vu comme un laser d'une longueur donné, "2f" dans ce cas, et qui doit toucher quelque chose pour retourné "true", à partir de la ".position" de "groundDetection". "groundDetection" étant un objet devant notre ennemi, il arrive dans le vide avant le sprite de ce dernier. 

Les composants de ce "Raycast" sont:
    1. Depuis où on l'envoie, "groundDetection.position"
    2. Comment on l'envoie, "Vector2.down", un vecteur (x y) -> (0 1)
    3. La longueur du vecteur

La deuxième partie utilise la propriété de bool du "groundInfo" pour enclencher le reste du code.

La dernière partie sert à changer la direction selon la direction actuelle. Pour cela, nous avons notre "private bool" "movingRight" qui nous permet de voir la direction. 

Ensuite, "Transform.eulerAngles" va inverser la direction de notre ennemi de "180" degrés. Cette fonction nécessite trois variables, même si le jeu est en 2D, car dans Unity, le "Transform" d'un objet contient "x,y,z". Il faut donc changer toutes ces variables. Pour finir, il suffit juste de changer le bool "movingRight".
##### 5. PlayerMovement.cs
##### 6. PlayerTeleport.cs
##### 7. Teleporter.cs

## Principaux fichiers
Il y a trois différents types de fichiers importants :
### 1. Scenes:
Ce fichier contient tous les différents niveaux dans notre jeu. Unity l'utilise pour afficher les différents sprites et nous permet de les construires. Cependant, il est automatiquement généré, ce qui veut dire que les fichiers inclus sont quasiment illisibles et nous ne pouvons pas le changer directement sans casser le jeu.
### 2. Script:
Ce fichier contient tous les scripts que nous avons créés. Il permet de voir l'intégralité de notre code dans 1 fichier et nous permet de facilement trouver les fichiers que l'on veut quand on créé un niveau. Il peut être considéré comme l'entry Point quand vous voulez analyser notre code.
### 3. GameObjects:
Ce fichier contient toutes les informations nécessaires à la création de l'environnement Unity. Il contient tous les éléments que nous avons utilisés et organisés pour faire notre niveau. Il permet aussi de nous faire gagner du temps en faisant passer certains traits, comme les layers, aux éléments plus bas dans le fichier, nous évitant de le faire manuellement.

## Concepts fondamentaux

### 1. Fonctionnement du logiciel Unity

Unity est un logiciel de création de jeux vidéo largement utilisé par les développeurs du monde entier pour concevoir des expériences interactives. Cette rubrique vise à expliquer les bases de son fonctionnement pour ceux qui souhaitent comprendre comment Unity peut être utilisé pour créer des jeux vidéo.

Unity repose sur un modèle de composants et d'objets. Dans ce modèle, les développeurs créent des "GameObjects" qui représentent des entités dans le jeu, comme des personnages, des objets ou des décors. Ces GameObjects sont ensuite enrichis de fonctionnalités grâce à des "Components" (composants) qui définissent leur comportement.

Les "Scènes" sont des environnements distincts dans lesquels évoluent les jeux créés avec Unity. Chaque scène peut contenir différents éléments tels que des personnages, des décors, etc. Les transitions entre les scènes permettent de créer des changements d'environnement et de narrative dans le jeu.

Unity intègre un système de physique réaliste qui permet de simuler les interactions entre les objets du jeu. Cela inclut la gestion de la gravité, des collisions, des forces, etc. Ce système donne aux développeurs la possibilité de créer des mouvements et des interactions crédibles dans le jeu. Ce système est utilisé afin de soumettre le joueur à la gravité. Il est retenu par la collision avec les platformes qui l'empêchent de tomber dans le vide. Il y a également des zones de "Trigger" qui fonctionnent comme les collision, mais elle servent seulement à détecter que deux GameObjects rentre en contact. Cependant un "Trigger" ne va pas retenir l'autre GameObject, ce dernier va continuer son chemin.

Unity supporte le scripting en C#, un langage de programmation largement utilisé. Les développeurs utilisent des scripts pour contrôler le comportement des GameObjects, implémenter la logique du jeu et gérer les interactions entre les différents éléments du jeu. Les scripts peuvent être attachés aux GameObjects pour définir leur comportement. Unity met aussi à disposition une API riche en fonctionnalités. ([API du scripting de Unity](https://docs.unity3d.com/ScriptReference/))

Unity permet l'utilisation d'une variété de ressources telles que des textures, des sons, des animations, etc. Ces ressources peuvent être importées dans le projet et utilisées pour enrichir le jeu. Unity offre également des outils intégrés pour éditer et manipuler ces ressources directement dans l'interface utilisateur. Cependant au vu de l'avancé du projet, il a été préférable de laisser de côté certains de ces aspects.

Comprendre le fonctionnement de Unity est essentiel pour quiconque souhaite créer des jeux vidéo. Avec ses fonctionnalités puissantes et son interface conviviale, Unity offre un environnement de développement robuste pour concrétiser des idées de jeu. Cette rubrique fournit donc une introduction aux principes fondamentaux de Unity pour ceux qui souhaitent explorer le monde fascinant de la création de jeux vidéo.

### 2. Formats de fichiers utilisés par Unity
Unity utilise plusieurs formats de fichiers pour stocker les données liées aux projets de jeux vidéo. Comprendre ces formats est important pour gérer efficacement les assets et les configurations du projet. Voici une brève explication des principaux formats de fichiers utilisés par Unity :

1. **.unity** : Les fichiers avec l'extension .unity sont des scènes Unity. Chaque fichier .unity correspond à une scène spécifique de votre jeu, où vous pouvez placer des GameObjects, des lumières, des caméras, etc. Ces fichiers contiennent des données de configuration de la scène et peuvent être ouverts et édités dans l'éditeur Unity.

2. **.meta** : Les fichiers .meta sont des fichiers de métadonnées associés à chaque asset dans votre projet Unity. Chaque asset (comme un modèle 3D, une texture, un script, etc.) a son propre fichier .meta qui contient des informations telles que son GUID unique (Globally Unique Identifier), son type, son nom, etc. Le GUID est un identifiant unique attribué à chaque asset lors de sa création dans Unity, ce qui permet à Unity de suivre les références entre les différents assets et de gérer les modifications apportées.

3. **.prefab** : Les fichiers .prefab sont des objets préfabriqués Unity. Un prefab est un GameObject complet avec tous ses composants et paramètres configurés, que vous pouvez réutiliser dans différentes scènes de votre projet. Les fichiers .prefab stockent les données de configuration du prefab, y compris les composants attachés et leurs paramètres.

Tous ces formats de fichiers sont basés sur le format de sérialisation YAML (YAML Ain't Markup Language). Le YAML est un format de texte simple et lisible par l'homme qui est utilisé par Unity pour stocker les données de configuration des projets. Cela rend les fichiers facilement lisibles et modifiables, que ce soit directement dans un éditeur de texte ou dans l'interface Unity.

En comprenant ces formats de fichiers et leur fonctionnement, les développeurs peuvent gérer efficacement les assets de leur projet, suivre les modifications et collaborer plus efficacement sur le développement du jeu.

### 3. UnityEngine.SceneManagement:
L'expression "UnityEngine.SceneManagement" est un namespace qui donne accès à des fonctionnalités liées à la gestion des scènes dans Unity.
Une "scène" dans Unity représente un environnement de jeu ou une partie spécifique d'un jeu, comme un niveau ou un menu. Le système de gestion des scènes permet de charger, décharger et manipuler différentes scènes pendant l'exécution du jeu.

En incluant "UnityEngine.SceneManagement", vous avez accès à des classes et des méthodes qui vous permettent de contrôler le chargement et la transition entre les scènes dans votre jeu. Par exemple, vous pouvez charger une nouvelle scène lorsque le joueur atteint un certain objectif, ou passer d'un niveau à un autre lorsque le joueur termine un niveau. Cela donne au développeur un contrôle précis sur la structure et le flux du jeu.

Prenons pour exemple le fichier "BuildScene.cs" :
```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class BuildScene : MonoBehaviour
{
    public void ChangeScene(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
        Time.timeScale = 1.0f;
    }
}
```
Il contient la méthode "SceneManager.LoadScene()" qui permet de recharger n'importe quelle scène qui a son nom dans les parenthèses. Ceci signifie que les éléments qui ont été changés se retrouve présents comme ils l'étaient la première fois que la scène a été chargée.

1. Il y a bien évidemment des propriétés qui sont dites statiques, dont certaines statiques:
    - SceneManagement.loadedSceneCount -> retourne le nombre de scènes chargées.
    - SceneManagement.sceneCount -> retourne le nombre de scènes.
    - SceneManagement.sceneCountInBuildSettings -> retourne le nombre de scène présentent dans les Build Settings (ceci est l'endroit dans lequel sont stockés les scènes qui seront utilisées lorsque le projet est construit/built).

2. Ensuite il y a d'autres méthodes qui sont statiques:
    - SceneManagement.CreateScene

    - SceneManagement.GetActiveScene
    - SceneManagement.SetActiveScene

    - SceneManagement.GetSceneAt

    - SceneManagement.GetSceneByBuildIndex
    - SceneManagement.GetSceneByName
    - SceneManagement.GetSceneByPath

    - SceneManagement.LoadScene -> précédemment présentée
    - SceneManagement.LoadSceneAsync -> charge la scène de manière asynchrone, en arrière plan, avec les autres scènes chargées.
    - SceneManagement.UnloadSceneAsync

    - SceneManagement.MergeScenes -> fusionne la scène source dans la scène de destination.

    - SceneManagement.MoveGameObjectsToScene -> permet de déplacer certains GameObject d'une scène à l'autre.
    - SceneManagement.MoveGameObjectToScene -> permet de déplacer un seul GameObject d'une scène à l'autre.

3. Finalement il reste trois événements pour le namespace "SceneManagement" sont:
    - SceneManagement.activeSceneChanged -> la scène souscrit à cet événement pour être notifié lorsque des scènes actives changent.

    - SceneManagement.sceneLoaded -> ajoute un délégué à cet événement d'être notifié d'une scène chargée.
    - SceneManagement.sceneUnloaded

Dans le cas de notre projet, le namespace est utilisé uniquement sur des boutons, qui ont pour objectif la navigation entre les différentes scènes, qui correspondent à des niveaux, ou à la page d'accueil du jeu.


### 4. StartCoroutine:
Une Coroutine est, dans Unity, une fonction qui dure pendant plusieurs secondes. 

Exemple FallingPlatform.cs :
```C#
public class FallingPlatform : MonoBehaviour
{
private float fallDelay = 0f;
private float destroyDelay = 2f;

[SerializeField] private Rigidbody2D rb;

private void OnCollisionEnter2D(Collision2D collision)
{
    if (collision.gameObject.CompareTag("Player"))
    {
        StartCoroutine(Fall());
    }
}

private IEnumerator Fall()
{
    yield return new WaitForSeconds(fallDelay);
    rb.bodyType = RigidbodyType2D.Dynamic;
    Destroy(gameObject, destroyDelay);
}
}
```
Dans cet exemple, la Coroutine est la fonction "Fall()". Avec "StartCoroutine()" "Fall()" va se lancer. Cependant, si "Fall()" était une fonction de base, la platforme tomberait immédiatement, mais, comme "Fall()" est une Coroutine, il faut attendre "fallDelay" secondes pour qu'elle tombe.


## Element problématique

### Akim
Selon moi, ce qui m'a le plus posé de problème a été de gérer l'emplacement des variables et des méthodes qui doivent être partagées entre certains GameObjects. En ce qui concerne le plus gros blocage, la direction des projectiles a été le plus inconvénient. Les projectiles partageaient tous la même direction, ce qui est problématique lorsque le joueur souhaite tirer deux projectiles dans des directions opposées.

Au départ le script "Shot" appartenait au joueur, étant donné que c'est à partir de sa direction que le projectile doit se diriger. Cependant tous les projectiles partageaient la direction du dernier projectile tiré. Il a fallu alors créer des prefab des projectiles qui ont eux aussi posés problème, puisque en réalité les projectiles sont simplement une copie d'un projectile de base qui lui doit rester constamment dans la scène. Car chaque projectile doit faire référence au script du joueur qui contient la direction actuelle.

C'est pourquoi il n'était pas possible d'instancier à chaque fois le prefab du projectile, mais à la place faire une copie du prefab qui est statique sur la scène.

### Louis
Pour moi, l'élément qui m'a posé le plus de problème était le script "Patrol.cs" qui a été analysé au-dessus. 

Pour commencer, j'avais l'idée de faire bouger l'ennemi entre 2 points prédéfinis. Cependant, cette méthode ne marchait pas quand le nombre d'ennemis était plus grand que 1, je ne sais pas pourquoi. Ensuite, j'ai utilisé une extension qui permettait de calculer la distance avec la fin de la plateforme, comme une limite qui s'approche de zéro pour la distance. Cependant, ce code ne marchait pas non plus. Pour finir, j'ai utilisé un "RayCast" pour voir si l'ennemi se situer encore sur la plateforme. 

Mais, avec cette version, nous avons perdu en modularité. 

En effet, avec la première version, nous aurions pu faire des ennemis qui vont de haut en bas, nous permettant d'ajouter d'autres fonctionnalités dans notre niveau, cela aurait été possible avec la première version. Maintenant, nos ennemis ne s'arrêtent que quand ils atteignent le bord d'une plateforme. 

Avec la deuxième version, ils s'arrêtaient aussi quand ils s'approchaient du joueur ou d'un obstacle prédéfinis. Nous aurions donc put les faire attaquer quand ils s'approchaient du joueur, ou faire une animation quand ils se retournaient.