## Cybersecurity Home Lab — Nmap & Firewall Test

**Date:** 2025-10-05  
**Attacker:** Windows host (Nmap)  
**Target:** Ubuntu lab (Host-only IP: 192.168.56.101)

> **Note:** All testing was done safely in an isolated home lab using VirtualBox virtual machines. No scans were performed on public or external systems.

---

## 1️⃣ Initial Baseline Scan
**Command used:**
`nmap -sV -p 1-1000 192.168.56.101 -oN nmap_initial.txt`

**Findings:**
- All ports closed — no active services found.

**Screenshot:**  
![Initial Nmap Scan](../screenshots/nmap_initial.png)

---

## 2️⃣ HTTP Server Detection
**Command used:**
`nmap -sV -p 8000 192.168.56.101 -oN nmap_with_http8000.txt`

**What I did:**  
- Started a basic HTTP server on the Ubuntu VM using Python (`python3 -m http.server 8000`).  
- Re-scanned the target machine to confirm the port was open.

**Findings:**  
- Port `8000/tcp` open — service detected: **SimpleHTTPServer 0.6 (Python 3.12.3)**

**Screenshot:**  
![Nmap with HTTP Server](../screenshots/nmap_with_http8000.png)

---


## 3️⃣ Firewall Configuration (UFW)
Enabled and configured UFW on Ubuntu to block port 8000.

**Commands executed:**
`sudo ufw --force enable`
`sudo ufw deny 8000/tcp`
`sudo ufw status numbered`

**What I did:**  
- Enabled Ubuntu’s Uncomplicated Firewall (UFW).  
- Added a rule to block incoming traffic on port 8000.  
- Verified the rule was active.
  
**Screenshot:**  
![UFW Status](../screenshots/ufw_status.png)


---

## 4️⃣ Verification Scan After Firewall
**Command used:**
`nmap -sV -p 8000 192.168.56.101 -oN nmap_after_ufw_block.txt`

**Findings:**  
- Port `8000/tcp` now filtered — confirmed that the firewall successfully blocked the HTTP server.

**Screenshot:**  
![Nmap After UFW Block](../screenshots/nmap_after_ufw_block.png)

---

### Summary
This lab helped me understand how firewalls interact with network scanning tools like Nmap.  
I learned how to:
- Safely perform network scans in a virtual lab environment,  
- Identify open and closed ports,  
- Configure and verify UFW firewall rules,  
- See the difference between open, closed, and filtered port states.  

---

### Next steps
- Keep practising with Nmap and UFW to get more confident using command-line tools.  
- Try adding more virtual machines to test how networks behave with multiple devices.  
- Learn more about how firewalls and ports work in real-life cybersecurity setups.
