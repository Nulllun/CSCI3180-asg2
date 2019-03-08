/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 2
 * Name : Lun Yin Fung
 * Student ID : 1155092566
 * Email Addr : 1155092566@link.cuhk.edu.hk
 */

 public class Potion{

        private static final int HEAL_CAP = 20;
	private Pos pos;
        private int index;
        private Map map;
        private String name;
        private int power;// the healing power
        
        public Potion(int posx, int posy, int index, Map map) {
                this.pos = new Pos(posx, posy);
                this.index = index;
                this.map = map;
                this.name = "P" + Integer.toString(index);
                this.power = TheJourney.rand.nextInt(HEAL_CAP - 5) + 5;
        }

        public boolean actionOnWarrior(Warrior warrior) {
                warrior.talk("Very good, I got additional healing potion " + this.getName() + ".");
                warrior.increaseHealth(this.getPower());
                if (warrior.getHealth() > 40){
                        // prevent the warrior health exceed the health cap
                        warrior.setHealth(40);
                }
                this.map.deleteTeleportableObj(this);
                // return True means the warrior will occupy this position
                return true;
        }

        public void teleport() {
                // the teleport function of the Potion
                this.map.setLand(this.getPos(), null);
                Pos newPos = this.map.getUnOccupiedPosition();
                this.pos.setPos(newPos.getX(), newPos.getY());
                this.map.setLand(this.getPos(), this);
        }

        public Pos getPos() {
		return pos;
        }
        
	public void setPos(Pos pos) {
		this.pos = pos;
        }
        
	public String getName() {
		return name;
        }
        
        public int getPower() {
		return power;
        }
        
}