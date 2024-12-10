public class Medium extends Collision
{
    public void processCollision(Projectile p, Enemy e) {
        p.setDelete();
        e.hit();
        int lives = e.getLives();
        if (lives == 1) {
            e.setColor();
        }
    }
    
}