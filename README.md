# Pan-Analysis-Killer
Solve the pan-analytic problem of subdomain name blasting in information collection
In information collection, this will create the illusion that all requested subdomains are accessible, thus collecting a bunch of invalid subdomains.
1. Identify pan-analytics
Randomly query several non-existent subdomain names to see if they resolve to the same IP. If so, there may be a pan-resolution
2. Exclude pan-analysis
Add the resolved IPs to the blacklist and filter out these IPs during the subdomain blasting process
3. Use CNAME records
Pan-resolved subdomains may not have CNAME records or point to the same target

解决信息收集中子域名爆破的泛解析问题
在信息收集中，这会造成请求的所有子域名都能访问的假象，从而收集到一堆无效的子域名
1. 识别泛解析
随机查询几个不存在的子域名，看是否解析到相同的IP，如果是，则可能存在泛解析
2. 排除泛解析
将解析出来的IP加入黑名单，在子域名爆破的过程中过滤掉这些IP
3.利用CNAME记录
泛解析的子域可能没有CNAME记录或者指向相同目标
