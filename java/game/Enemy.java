import edu.nd.cse.paradigms.*;

public class Enemy extends PESquare
{
    int dx;
    int dy;
    int lives;

    public Enemy(int dx, int dy, int difficulty)
    {
        this.dx = dx;
        this.dy = dy;
        this.lives = difficulty;
    }

    public void tick()
    {
        int x = this.getX();
        int y = this.getY();
        x += this.dx;
        y -= this.dy;
        if (x < 30 || x > 610) {
            this.dx = -this.dx;
            x += this.dx;
            x += this.dx;
        }
        if (y < 30 || y > 450) {
            this.dy = -this.dy;
            y -= this.dy;
            y -= this.dy;
        }
        this.setCenter(x, y);
    }

    public int getLives() {
        return this.lives;
    }

    public void hit() {
        this.lives -= 1;
    }

    public void setColor() {
        if (lives == 1) {
            this.setColor(0xDE2A2A);
        } else if (lives == 2) {
            this.setColor(0xF0EC2B);
        }
    }
}