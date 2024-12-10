import edu.nd.cse.paradigms.*;

public abstract class Collision 
{
    public abstract void processCollision(Projectile p, Enemy e);

    public void collide(Projectile p, Enemy e)
    {
        this.processCollision(p, e);
    }
}