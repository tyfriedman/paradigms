package edu.nd.cse.paradigms;

import java.awt.*;

public class PEEngine extends Frame
{
   protected PEGame game;
   protected PEScreen screen;
   protected int width = 640;
   protected int height = 480;
   protected int titlebarHeight = 0; // varies by OS
	
   public PEEngine(PEGame game)
   {
      this.game = game;
      this.width = width;  
      this.height = height;
      this.screen = new PEScreen(this.height, this.width);
   }
   
   public void tick() {
   }

   public void paint(Graphics g)
   {
       g.drawImage(screen.render(), 0, titlebarHeight, width, height, Color.BLACK, null);
   }
}
