public class Easy extends Collision
{
    public void processCollision(Projectile p, Enemy e) {
        p.setDelete();
        e.hit();
    }
}