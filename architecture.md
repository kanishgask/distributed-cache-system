# Distributed Cache Architecture

Client
 ↓
Load Balancer
 ↓
Cache Nodes (Cluster)
 ↓
Database (Fallback)

---

# Flow

1 Client requests data  
2 Cache checked  
3 If HIT → return data  
4 If MISS → fetch from DB  
5 Store in cache  

---

# Scaling Strategy

• Consistent hashing for node distribution  
• Multiple cache nodes  
• Replication for fault tolerance  
• LRU eviction for memory control
