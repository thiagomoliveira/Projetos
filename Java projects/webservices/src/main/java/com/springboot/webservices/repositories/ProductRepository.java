package com.springboot.webservices.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.webservices.entities.Product;

public interface ProductRepository extends JpaRepository<Product, Long>{

}
