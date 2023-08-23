package com.springboot.webservices.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.webservices.entities.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Long>{

}
