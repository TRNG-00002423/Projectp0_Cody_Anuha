package com.revature.service;

import com.revature.dao.UserDao;
import com.revature.model.User;
import org.mindrot.jbcrypt.BCrypt;

import java.util.Optional;

public class LoginService {

    private final UserDao userDao;

    public LoginService(UserDao userDao) {
        this.userDao = userDao;
    }

    public Optional<User> login(String username, String plaintextPassword) {
        Optional<User> userOpt = userDao.findByUsername(username);

        if (userOpt.isEmpty()) {
            return Optional.empty();
        }

        User user = userOpt.get();

        boolean matches = BCrypt.checkpw(plaintextPassword, user.getPassword());

        if (!matches) {
            return Optional.empty();
        }

        return Optional.of(user);
    }
}