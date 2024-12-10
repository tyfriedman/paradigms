package edu.nd.cse.paradigms;

import java.awt.*;
import java.util.TimerTask;
import java.util.Timer;

public class PECentralClock extends TimerTask
{
    protected PEEngine engine;
    private int rate;
    private Timer timer;

    public PECentralClock(PEEngine engine, int rate) {
        this.engine = engine;
        this.rate = rate;
        this.timer = new Timer(true);
		timer.scheduleAtFixedRate(this, 0, rate);
    }

    public void run() {
        this.engine.tick();
    }
}