package com.springboot.webservices.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.webservices.entities.User;

public interface UserRepository extends JpaRepository<User, Long>{

}
