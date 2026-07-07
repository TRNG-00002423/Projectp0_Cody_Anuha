package com.revature.controller;

import com.revature.model.User;
import com.revature.service.LoginService;

import java.util.Optional;

public class AuthController {

    private final LoginService loginService;

    public AuthController(LoginService loginService) {
        this.loginService = loginService;
    }

    public User login(String username, String password) {
        Optional<User> userOpt = loginService.login(username, password);

        return userOpt.orElseThrow(() ->
                new SecurityException("Invalid username or password"));
    }
}