# Tips for KennaSecurity Search Syntax

I'm sharing some of my tips that I used to search (and create meters) in KennaSecurity. Here, you will find some tips that not available in KennaSecurity help pages.

### :bulb: Kenna Score
> Quick tips on how [Kenna Score](Kenna-Score.md) works!

### :bulb: Excluding asset from the meter score 
> Sometimes you need to exclude some assets from participating in the (average) Kenna meter score, but you still like those asset to be shown in the same Kenna meter. Just set the (individual) asset priority to 0, and the Kenna meter score won't take into account for those asset (with priority 0). This is a handy way to manage the Kenna meter score without making big change.

### :bulb: Active_breach/Easily_exploit/Malware/Popular/Top_priority
> To search any vulnerability that are belongs to Active Internet breaches, easily exploitable, malware exploitable, popular target and top priority.
```sql
    active_internet_breach:true AND easily_exploitable:true AND malware_exploitable:true AND popular_target:true AND top_priority:true
```


### :bulb: Unmappable Vulnerability
> To list any unmappable vulnerability. 
```sql
    vulnerability_name:"Unmappable Vulnerability" AND vulnerability_score:>1
```


### :bulb: Pre-NVD Chatter 
> To search any threats that are not yet published in NVD or scored in CVSS. This can help us to manage newly disclosed vulnerabilities, even before they're published on the National Vulnerability Database (NVD), so we can proactively managing the vulnerabilties.
```sql
    cve_description:"This candidate has been reserved"
```


### :bulb: Empty Asset
> To list those weird assets in Kenna (without hostname, nor IP, nor URL).
```sql
    -_exists_:hostname AND -_exists_:IP AND -_exists_:url
```


### :bulb: Empty TAG 
> To list those asset that has no tag at all. 
```sql
    -tag:"*"
```


### :bulb: Empty OS 
> To list those asset that with no OS.
```sql
    -os:?*
```


### :bulb: Vulnerability without Fix
> To list those vulnerability that without any fix or solution.
```sql
    -_exists_:fix AND vulnerability_score:>0 
```


### :bulb: Vulnerabilities closed within SLA 
> To list those vulnerabilities that closed within the SLA in the past 45 days. 
```sql
    closed_at:>now-45d AND _exists_:due_date AND not_closed_by_due_date:false
```


### :bulb: Check if SLA is working (vulnerability without Due Date)
> If SLA is working fine, every vulnerability should have a due date. This is to list any vulnerability that has no due date. 
```sql
    -due_date:"*"
```


### :bulb: Vulnererability older than Asset Last Seen
> Assuming your "Asset Inactivity Limit" (within Asset Settings) is set to 31 days, this syntax here is to find out any vulnerability is older than asset's last seen date. This useful to find out those vulnerabilities that not closed by KennaSecurity automatically. It can be used to discover if the asset has been scanned correctly (with credential) or not.
```sql
    vulnerability_last_seen:<now-31d
```


### :bulb: Vulnererability older than Asset Last Seen
> Assuming your "Asset Inactivity Limit" (within Asset Settings) is set to 31 days, this syntax here is to find out any vulnerability is older than asset's last seen date. This useful to find out those vulnerabilities that not closed by KennaSecurity automatically. It can be used to discover if the asset has been scanned correctly (with credential) or not.
```sql
    vulnerability_last_seen:<now-31d
```

### :bulb: Vulnerability that could be exploited in the near future (hidden)
> If you want to be more aggresive in prioritizing your vulnerability remediation, this is a useful (hidden) feature for you. For normal remediation, we can prioritize the remediation based on exploitability. With this option, we can filter those vulnerabilities that may potentially be exploitable in the future. This is based on Kenna proprietary algorithm. 
```sql
    predicted_exploitable:true
```


