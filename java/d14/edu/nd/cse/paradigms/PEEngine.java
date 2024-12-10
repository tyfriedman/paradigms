package edu.nd.cse.paradigms;

import java.awt.*;
import java.util.List;
import java.util.ArrayList;

public class PEEngine extends Frame
{
   protected PEGame game;
   protected PEScreen screen;
   protected int width;
   protected int height;
   protected int titlebarHeight; // varies by OS
   protected List<PEWorldObject> worldObjects;
   protected PECentralClock clock;
	
   public PEEngine(PEGame game, int rate)
   {
      this.width = 640;
      this.height = 480;
      this.titlebarHeight = 0;

      this.game = game;
      this.screen = new PEScreen(this.height, this.width);
      this.screen.clear();

      this.worldObjects = new ArrayList<>();
      // this.clock = new PECentralClock(this, rate);

      // screen.clear();

      setSize(width, height+titlebarHeight);
      setVisible(true);

      this.clock = new PECentralClock(this, rate);
   }

   public void add(PEWorldObject wo) {
      this.worldObjects.add(wo);
   }

   public void remove(PEWorldObject wo) {
      this.worldObjects.remove(wo);
   }

   public void tick() {
      this.game.tick();
      this.screen.clear();
      for (PEWorldObject wo : worldObjects) {
         wo.tick();
         wo.render(this.screen);
      }
      this.repaint();
   }

   public void update(Graphics g) {
      this.paint(g);
   }

   public void paint(Graphics g)
   {
       g.drawImage(screen.render(), 0, titlebarHeight, width, height, Color.BLACK, null);
   }
}
