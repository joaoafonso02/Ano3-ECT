import java.security.Provider;
import java.security.Security;

public class ex2 {
    public static void main(String[] args){
	Provider p = Security.getProvider("SunPKCS11");
	p = p.configure("CitizenCard.cfg");
	Security.addProvider(p) ;
    }
}
