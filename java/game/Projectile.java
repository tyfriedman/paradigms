import edu.nd.cse.paradigms.*;

public class Projectile extends PECircle
{
    int x;
    int y;
    int tx; 
    int ty;
    int size = 5;
    PEEngine engine;
    boolean delete = false;

    public Projectile(PEEngine engine, int x, int y, int tx, int ty)
    {
        this.x = x;
        this.y = y;
        this.tx = tx;
        this.ty = ty;
        this.setRadius(size);
		this.setCenter(x, y);
		this.setColor(0xFFFFFF);
        this.engine = engine;
    }

    public void tick() {
        int dx = this.tx - this.x;
        int dy = this.ty - this.y;

        double distance = Math.sqrt(dx * dx + dy * dy);
        if (distance <= 4) {
            this.delete = true;
            return;
        }

        if (distance != 0) {
            dx = (int)(7 * dx / distance);
            dy = (int)(7 * dy / distance);
            this.x += dx;
            this.y += dy;
            this.setCenter(this.x, this.y);
        }
    }

    public boolean getDelete() {
        return this.delete;
    }

    public void setDelete() {
        this.delete = true;
    }

}