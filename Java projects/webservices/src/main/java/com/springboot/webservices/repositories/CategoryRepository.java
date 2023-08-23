package com.springboot.webservices.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.webservices.entities.Category;

public interface CategoryRepository extends JpaRepository<Category, Long>{

}
