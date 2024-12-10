import edu.nd.cse.paradigms.*;

import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame
{
	protected PEEngine engine;
	private Collision collisionStrategy;

	private Player player;
	private Enemy enemy1;
	private Enemy enemy2;
	private int difficulty;
	private Projectile projectile;
	
	public MyGame(int difficulty)
	{
		this.difficulty = difficulty;
		if (difficulty == 1) {
			this.collisionStrategy = new Easy();
		} else if (difficulty == 2) {
			this.collisionStrategy = new Medium();
		} else {
			this.collisionStrategy = new Hard();
		}
	}

	public void start()
	{
		engine = new PEEngine(this, 50);

		player = new Player(engine);
		player.setRadius(20);
		player.setCenter(25, 25);
		player.setColor(0xFFFFFF);
		engine.add(player);

		enemy1 = new Enemy(1, 1, this.difficulty);
		enemy1.setSize(100);
		enemy1.setCenter(100, 300);
		enemy1.setColor(0xCCAAFF);
		engine.add(enemy1);

		enemy2 = new Enemy(-1, 2, this.difficulty);
		enemy2.setSize(70);
		enemy2.setCenter(400, 100);
		enemy2.setColor(0xCCAAFF);
		engine.add(enemy2);
	}

	public void tick()
	{
		if (this.projectile != null && this.projectile.getDelete() == true) {
			this.engine.remove(this.projectile);
			this.projectile = null;
		}
		if (this.enemy1 != null && this.enemy1.getLives() == 0) {
			this.engine.remove(this.enemy1);
		}
		if (this.enemy2 != null && this.enemy2.getLives() == 0) {
			this.engine.remove(this.enemy2);
		}
	}

	/**
	 * This function is called by the engine whenever a key is pressed.
	 */
	public void keyPressed(int keycode)
	{
		int px = player.getX();
		int py = player.getY();
		int ax = player.getAx();
		int ay = player.getAy();

		switch(keycode)
		{
			case PEKeyEvent.VK_DOWN:
				py += 5;
				break;
            case PEKeyEvent.VK_LEFT:
                px -= 5;
                break;
            case PEKeyEvent.VK_RIGHT:
                px += 5;
                break;
            case PEKeyEvent.VK_UP:
                py -= 5;
                break;
			case 87:
				ay -= 5;
				break;
			case 83:
				ay += 5;
				break;
			case 65:
				ax -= 5;
				break;
			case 68:
				ax += 5;
				break;
			case 32:
				if (this.projectile == null && this.player.getAlive() == true) {
					this.projectile = new Projectile(this.engine, this.player.getX(), this.player.getY(), this.player.getAx(), this.player.getAy());
					this.engine.add(projectile);
				}
		}

		player.setCenter(px, py);
		player.setAim(ax, ay);
	}
	
	public void collisionDetected(List<PEWorldObject> objects)
	{
		boolean attack = false;
		PEWorldObject worldObject1 = objects.get(0);
		PEWorldObject worldObject2 = objects.get(1);

		if ((worldObject1 instanceof Player || worldObject2 instanceof Player) && (worldObject1 instanceof Enemy || worldObject2 instanceof Enemy)) {
			this.engine.remove(this.player);
			this.player.died();
		} else if ((worldObject1 instanceof Projectile) && (worldObject2 instanceof Enemy)) {
			Projectile p = (Projectile)worldObject1;
			Enemy e = (Enemy)worldObject2;
			this.collisionStrategy.collide(p, e);
		} else if ((worldObject2 instanceof Projectile) && (worldObject1 instanceof Enemy)) {
			Projectile p = (Projectile)worldObject2;
			Enemy e = (Enemy)worldObject1;
			this.collisionStrategy.collide(p, e);
		}
	}
}
