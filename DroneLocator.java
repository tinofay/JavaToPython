
import java.util.concurrent.TimeUnit;

public class DroneLocator {

    public static void main(String args[]) {
        
        droneMoves(11);
        
    }
    
    public static void droneMoves(int givenInput){
        
        long startTime = System.nanoTime();
        
        
        long timeInFlight =System.nanoTime() - startTime;
        
        int xCurrentPosition = 0;
        int yCurrentPosition = 1;
        
        int r = 0;
        int upConst = 1;
        int leftIncrement = 1;
        int downIncrement = 1;
        int leftConst = 1;
        int upIncrement = 2;
        int rightIncrement = 2;
        
    while(r <= givenInput){
          
    yCurrentPosition = yCurrentPosition + upConst;
    r = r + upConst;
    if (r > givenInput) {
    int difference = r - givenInput;
    yCurrentPosition = yCurrentPosition - difference;
    break;
    }

    xCurrentPosition = xCurrentPosition + leftIncrement;
    r = r + leftIncrement;
    
    leftIncrement = leftIncrement + 2;
    
    if (r > givenInput) {
    int difference = r - givenInput;
    xCurrentPosition = xCurrentPosition - difference;
    break;
    }

    yCurrentPosition = yCurrentPosition - downIncrement;
    r = r + downIncrement;
    downIncrement = downIncrement +2;
    
    if (r > givenInput) {
    int difference = r - givenInput;
    yCurrentPosition = yCurrentPosition+ difference;
    break; 
    }

    xCurrentPosition = xCurrentPosition + leftConst;
    r = r + leftConst;
    
    if (r > givenInput) {
    int difference = r - givenInput;
    xCurrentPosition = xCurrentPosition - difference;
    break;
    }

    yCurrentPosition = yCurrentPosition+ upIncrement;
    r = r + upIncrement;
    upIncrement = upIncrement + 2;
    
    if (r > givenInput) {
    int difference = r - givenInput;
    yCurrentPosition = yCurrentPosition - difference;
    break;
    }

    xCurrentPosition = xCurrentPosition - rightIncrement;
    r = r + rightIncrement;
    rightIncrement = rightIncrement + 2;
    
    if (r > givenInput) {
    int difference = r - givenInput;
    xCurrentPosition = xCurrentPosition + difference;
    break;
    }
}
            
            System.out.println(xCurrentPosition + " X metres left");
            System.out.println(yCurrentPosition + "Y  metres forward");
            System.out.println("elapsed time in millis " + TimeUnit.SECONDS.convert(timeInFlight, TimeUnit.NANOSECONDS)/1000000);
        }
        
       
          
       
    
}
