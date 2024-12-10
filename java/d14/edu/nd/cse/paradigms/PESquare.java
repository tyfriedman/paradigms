package edu.nd.cse.paradigms;

import java.awt.*;

public class PESquare extends PEWorldObject
{
    private int size;

    public PESquare() {};

    public void setSize(int size) 
    {
        this.size = size;
    }

    public void tick() {}
    
    public void render(PEScreen screen) {
        for (int i = this.x - (size/2); i <= this.x + (size/2); i++) {
            for (int j = this.y - (size/2); j <= this.y + (size/2); j++) {
                screen.setPixel(i, j, this.color);
            }
        }
    }
}