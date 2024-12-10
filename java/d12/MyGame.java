import edu.nd.cse.paradigms.*;

import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame
{
	protected PEEngine engine;

	// game objects
	private PECircle circle;
	private PESquare square;

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

		square = new PESquare();
		square.setSize(20);
		square.setCenter(25, 200);
		square.setColor(0xCCAAFF);
		engine.add(square);

	}

	public void tick()
	{
	}

	/**
	 * This function is called by the engine whenever a key is pressed.
	 */
	public void keyPressed(int keycode)
	{
		int x = circle.getX();
		int y = circle.getY();

		switch(keycode)
		{
			case PEKeyEvent.VK_DOWN:
				y += 5;
				break;
            case PEKeyEvent.VK_LEFT:
                x -= 5;
                break;
            case PEKeyEvent.VK_RIGHT:
                x += 5;
                break;
            case PEKeyEvent.VK_UP:
                y -= 5;
                break;
		}

		circle.setCenter(x, y);
	}
	
	public void collisionDetected(List<PEWorldObject> worldObjects)
	{
		engine.remove(circle);
	}
}
