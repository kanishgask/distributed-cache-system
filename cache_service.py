# ⚡ Distributed Cache System

System Design Project – High Performance Caching Layer

---

# Problem Statement

Design a distributed cache system to store frequently accessed data in memory to reduce database load and improve response time.

---

# Functional Requirements

• Store key-value pairs  
• Retrieve cached data  
• Evict old data when memory is full  
• Support distributed caching  

---

# Non Functional Requirements

• Low latency (<10ms)  
• High availability  
• Scalability  
• Fault tolerance  

---

# Core Concepts

• In-memory caching  
• Consistent hashing  
• Cache eviction (LRU)  
• Horizontal scaling  

---

# High Level Architecture

Client
 ↓
API Gateway
 ↓
Cache Cluster
 ↓
Database (fallback)
