import edu.nd.cse.paradigms.*;
import java.util.Random;

public class PowerupFactory extends PEShapeFactory
{
    private Random rand;

    public PowerupFactory() 
    {
        this.rand = new Random();
    }

    public PESquare createShape() 
    {
        PESquare powerup = new PESquare();
        int x = rand.nextInt(640);
        int y = rand.nextInt(480);
        powerup.setCenter(x, y);
        powerup.setSize(10);
        powerup.setColor(0xFFD700);
        return powerup;
    }
}