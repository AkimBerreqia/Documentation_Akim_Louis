# Explications

## Travail effectué

***Pour chaque fichier .cs (qui sont ceux dans lesquels nous avons codé), le code source est répertorié sur le dépôt GitHub du projet. [Code source du projet OC_projet_Akim_Louis](https://github.com/AkimBerreqia/OC-projet-Akim-Louis/tree/main/OC_projet_Akim_Louis/Assets/Script)***

### Akim

#### fichiers
##### 1. WinGame.cs:
- Ce fichier contrôle si le joueur rentre en collision avec le "Roasty Meat". Si c'est le cas, alors la méthode "Win()" se lance et affiche le menu de victoire.
##### 2. UnlockBlockingPlatforms.cs:
- Quant à ce fichier, il contient l'integer "lockers", qui est égal à l'integer "lockers" du fichier Blocker.cs pour chaque update.
##### 3. StartGame.cs:
- Ce fichier est utilisé pour le Home Menu. Il contient trois méthodes. La première,"ChooseLevel()", est utilisée quand le button "CHOOSE LEVEL" est enclenché. Cela cache la fenêtre d'accueil pour montrer la fenêtre de choix de niveau.
- La deuxième méthode, "Back()", fait l'action inverse de "ChooseLevel()".
- Et pour la dernière méthode, "QuitGame()", elle ferme l'application. 
##### 4. Shot.cs:
- Dans ce fichier, il y a des informations qui font références aux différents composants et objets nécessaires au script.
- Ensuite, il y a des variables publiques pour le projectile lié au script et le mouvement du joueur, puisque la direction du joueur influence le point de départ du projectile. En général, le script s'occupe d'ordonner les actions de chaque projectile (déplacement et possède le script pour attaquer un ennemi). Si le projectile est rouge et qu'il touche un ennemi, alors le booléen "isFired" est vrai. Ce booléen provient du script de l'ennemi touché, afin qu'il continue de subir des dégâts sur la durée.
- Suivant le type de projectile, le projectile est visible ou non. Par exemple les projectiles vert sont des bonus au joueur, donc ils sont invisibles, puisqu'ils ne servent pas à attaquer.
- Si le projectile est vert, alors le prochain a un bonus sur sa vitesse de déplacement et ses dégâts.
##### 5. SetHealth.cs:
- 
##### 6. Projectile.cs
##### 7. Power.cs
##### 8. PlayerHealth.cs
##### 9. MedicalKitNumber.cs
##### 10. Mana.cs
##### 11. ItemsMovement.cs
##### 12. GameOverAndPauseMenu.cs
##### 13. EnterBlockingPlatform.cs
##### 14. EnemyLife.cs
##### 15. Enemy.cs
##### 16. BossEmergence.cs
##### 17. BuildScene.cs
##### 18. Blocker.cs
### Louis

Je me suis occupé du mouvement du joueur et des ennemis ainsi que de la construction des niveaux.
#### fichiers
##### 1. CameraFollow.cs
##### 2. FallingPlatform.cs
##### 3. JumpPad.cs
##### 4. Patrol.cs
##### 5. PlayerMovement.cs
##### 6. PlayerTeleport.cs
##### 7. Teleporter.cs

## Principaux fichiers
Il y a trois différents types de fichiers importants :
### 1. Scenes:
- Ce fichier contient tous les différents niveaux dans notre jeu. Unity l'utilise pour afficher les différents sprites et nous permet de les construires. Cependant, il est automatiquement généré, ce qui veut dire que les fichiers inclus sont quasiment illisibles et nous ne pouvons pas le changer directement sans casser le jeu.
### 2. Script:
- Ce fichier contient tous les scripts que nous avons créés. Il permet de voir l'intégralité de notre code dans 1 fichier et nous permet de facilement trouver les fichiers que l'on veut quand on créé un niveau. Il peut être considéré comme l'entry Point quand vous voulez analyser notre code.
### 3. GameObjects:
- Ce fichier contient toutes les informations nécessaires à la création de l'environnement Unity. Il contient tous les éléments que nous avons utilisés et organisés pour faire notre niveau. Il permet aussi de nous faire gagner du temps en faisant passer certains traits, comme les layers, aux éléments plus bas dans le fichier, nous évitant de le faire manuellement.

## Concepts fondamentaux

### Akim
#### 1. UnityEngine.SceneManagement:
- L'expression "UnityEngine.SceneManagement" est un namespace qui donne accès à des fonctionnalités liées à la gestion des scènes dans Unity.
    Une "scène" dans Unity représente un environnement de jeu ou une partie spécifique d'un jeu, comme un niveau ou un menu. Le système de gestion des scènes permet de charger, décharger et manipuler différentes scènes pendant l'exécution du jeu.

    En incluant "UnityEngine.SceneManagement", vous avez accès à des classes et des méthodes qui vous permettent de contrôler le chargement et la transition entre les scènes dans votre jeu. Par exemple, vous pouvez charger une nouvelle scène lorsque le joueur atteint un certain objectif, ou passer d'un niveau à un autre lorsque le joueur termine un niveau. Cela donne au développeur un contrôle précis sur la structure et le flux du jeu.

    Prenons pour exemple le fichier "BuildScene.cs". Il contient la méthode "SceneManager.LoadScene()" qui permet de recharger n'importe quelle scène qui a son nom dans les parenthèses. Ceci signifie que les éléments qui ont été changés se retrouve présents comme ils l'étaient la première fois que la scène a été chargée.

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

- Dans le cas de notre projet, le namespace est utilisé uniquement sur des boutons, qui ont pour objectif la navigation entre les différentes scènes, qui correspondent à des niveaux, ou à la page d'accueil du jeu.


### Louis
#### 1. StartCoroutine:
- Une Coroutine est, dans Unity, une fonction qui dure pendant plusieurs secondes. 

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

## Explication du code

### Akim

### Louis
Pour cette partie j'expliquerai le fichier "Patrol.cs"

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

Ensuite, "Transform.eulerAngles" va inverser la direction de notre ennemi de "180" degrés. Cette fonction nécessite trois variables, même si le jeu est en 2D, car dans Unity, le "Transform" d'un objet contient "x,y,z". Il faut donc changer toutes ces variables. Pour finir, il suffit juste de changer le bool "movingRight"
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