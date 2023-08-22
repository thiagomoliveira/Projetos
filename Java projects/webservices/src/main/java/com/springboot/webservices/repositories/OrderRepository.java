package com.springboot.webservices.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.webservices.entities.Order;

public interface OrderRepository extends JpaRepository<Order, Long>{

}
