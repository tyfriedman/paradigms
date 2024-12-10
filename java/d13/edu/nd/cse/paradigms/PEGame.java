package edu.nd.cse.paradigms;

public class PEGame
{
   protected PEEngine engine;
   
   public PEGame()
   {
      this.engine = new PEEngine(this);
   }
}
