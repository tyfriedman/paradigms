public class Hard extends Collision
{
    public void processCollision(Projectile p, Enemy e) {
        p.setDelete();
        e.hit();
        int lives = e.getLives();
        if (lives > 0) {
            e.setColor();
        }
    }
}