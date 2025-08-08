import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

    @Test
    public void testMainRuns() {
        // 模拟调用 Main.main() 方法
        try {
            Main.main(new String[]{});
        } catch (Exception e) {
            fail("Main.main() should not throw an exception");
        }
    }
}
