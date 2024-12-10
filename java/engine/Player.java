import edu.nd.cse.paradigms.*;

public class Player extends PECircle
{
    PESquare aimer;
    PEEngine engine;
    int ax;
    int ay;
    boolean alive = true;

    public Player(PEEngine engine)
    {
        this.engine = engine;
        aimer = new PESquare();
		aimer.setSize(10);
        ax = 100;
        ay = 100;
		aimer.setCenter(ax, ay);
		aimer.setColor(0xFF0000);
		engine.add(aimer);
    }

    public int getAx()
    {
        return this.ax;
    }

    public int getAy()
    {
        return this.ay;
    }

    public void setAim(int x, int y)
    {
        this.aimer.setCenter(x, y);
        this.ax = x;
        this.ay = y;
    }

    public void tick()
    {
    }

    public void died() {
        this.alive = false;
    }

    public boolean getAlive() {
        return this.alive;
    }

    public int getRadius() {
        return this.radius;
    }

}