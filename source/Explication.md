# Explications

## Travail effectué

### Akim

#### fichiers
1. WinGame.cs
2. UnlockBlockingPlatforms.cs
3. StartGame.cs
4. Shot.cs
5. SetHealth.cs
6. Projectile.cs
7. Power.cs
8. PlayerHealth.cs
9. MedicalKitNumber.cs
10. Mana.cs
11. ItemsMovement.cs
12. GameOverAndPauseMenu.cs
13. EnterBlockingPlatform.cs
14. EnemyLife.cs
15. Enemy.cs
16. BossEmergence.cs
17. BuildScene.cs
18. Blocker.cs
### Louis

Je me suis occupé du mouvement du joueur et des ennemis ainsi que de la construction des niveaux.
#### fichiers
1. CameraFollow.cs
2. FallingPlatform.cs
3. JumpPad.cs
4. Patrol.cs
5. PlayerMovement.cs
6. PlayerTeleport.cs
7. Teleporter.cs

## Principaux fichiers

## Concepts fondamentaux

### Akim

### Louis
1. StartCoroutine:
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
    Dans cet exemple, la Coroutine est la fonction "Fall()". Avec "StartCoroutine()" "Fall()" va se lancer. Cependant, si "Fall()" était une fonction de base, la platforme tomberait immédiatemment, mais, comme "Fall()" est une Coroutine, il faut attendre "fallDelay" secondes pour qu'elle tombe.

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
Ce fichier permet de faire patrouiller un ennemi sur un platforme.

Il est diviser en 3 parties:
    
    
    1. Appelation des variables
    2. mouvement de l'ennemi
    3. informations nécessaire pour le mouvement 

La première partie contient toute les informations nécessaire au bon fonctionnement du code. Les deux premières lignes permettent de customiser notre ennemi grâce au code fait par Akim, ensuite nous pouvons customiser la vitesse de l'ennemi et la direction dans laquelle il va se diriger au lancement du jeu. Le public Transform nous permet de référencer un élément accrocher à notre "Player". 
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
## Element problématique

### Akim

### Louis