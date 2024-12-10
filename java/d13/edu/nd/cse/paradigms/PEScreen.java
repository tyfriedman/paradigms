package edu.nd.cse.paradigms;

import java.awt.image.BufferedImage;

public class PEScreen
{
   private int width, height;
   private int bg;
	
   private BufferedImage image;
   private int[][] pixels;
	
   public PEScreen(int width, int height)
   {
       this.width = width;
       this.height = height;
		
       this.bg = 0x22CC11; // default background color is green

       pixels = new int[height][width];

       clear();
   }
	
   public void setPixel(int px, int py, int color)
   {
       pixels[py][px] = color;
   }
	
   public void clear()
   {
       for (int y = 0; y < height; y++) {
           for (int x = 0; x < width; x++) {
               pixels[y][x] = bg;
           }
       }
   }
	
   public boolean inBounds(int px, int py)
   {
      if (px < width && py < height) {
         return true;
      } else {
         return false;
      }
   }
	
   public BufferedImage render()
   {
      if (image == null) {
           image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
       }
	   
       for (int y = 0; y < height; y++) {
           for (int x = 0; x < width; x++) {
               image.setRGB(x, y, pixels[y][x]);
           }
       }
		
       return image;
   }
}
