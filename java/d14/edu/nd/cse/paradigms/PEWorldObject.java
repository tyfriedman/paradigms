package edu.nd.cse.paradigms;

import java.awt.*;

abstract public class PEWorldObject 
{
    public int color;
    public int x;
    public int y;

    public PEWorldObject() {};

    public void setCenter(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void setColor(int color) {
        this.color = color;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }

    public abstract void tick();

    public abstract void render(PEScreen screen);
}
