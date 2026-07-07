package controller;

import com.revature.dao.UserDao;
import com.revature.model.Role;
import com.revature.model.User;
import com.revature.service.LoginService;
import com.revature.controller.AuthController;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mindrot.jbcrypt.BCrypt;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class AuthControllerTest {

    private UserDao userDao;
    private AuthController authController;

    @BeforeEach
    void setUp() {
        userDao = mock(UserDao.class);
        LoginService loginService = new LoginService(userDao);
        authController = new AuthController(loginService);
    }

    @Test
    void loginSucceedsWithCorrectPassword() {
        String hashedPassword = BCrypt.hashpw("password", BCrypt.gensalt());
        User fakeUser = new User(1, "admin", hashedPassword, Role.MANAGER);

        when(userDao.findByUsername("admin")).thenReturn(Optional.of(fakeUser));

        User result = authController.login("admin", "password");

        assertEquals("admin", result.getUsername());
        assertEquals(Role.MANAGER, result.getRole());
    }

    @Test
    void loginFailsWithWrongPassword() {
        String hashedPassword = BCrypt.hashpw("password", BCrypt.gensalt());
        User fakeUser = new User(1, "admin", hashedPassword, Role.MANAGER);

        when(userDao.findByUsername("admin")).thenReturn(Optional.of(fakeUser));

        SecurityException ex = assertThrows(SecurityException.class,
                () -> authController.login("admin", "wrongpassword"));

        assertEquals("Invalid username or password", ex.getMessage());
    }

    @Test
    void loginFailsWithUnknownUsername() {
        when(userDao.findByUsername("nosuchuser")).thenReturn(Optional.empty());

        SecurityException ex = assertThrows(SecurityException.class,
                () -> authController.login("nosuchuser", "anything"));

        assertEquals("Invalid username or password", ex.getMessage());
    }
}