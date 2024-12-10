import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;
public class MyGame extends PEGame
{
    protected PEEngine engine;
    public PECircle circle;

    public MyGame()
    {
    }

    public void start()
    {
        engine = new PEEngine(this);
        circle = new PECircle();
        circle.setRadius(25);
        circle.setCenter(25, 25);
        circle.setColor(0xFFFFFF);
        engine.add(circle);
    }

    public void tick()
    {
    }

    public void keyPressed(int keycode)
    {
        int x = circle.getX();
        int y = circle.getY();
        circle.setCenter(x, y+5);
    }

    public void collisionDetected(List<PEWorldObject> worldObjects)
    {
    }
}


