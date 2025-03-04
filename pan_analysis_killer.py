import asyncio
import aiodns
import random
import optparse
import platform

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
resolver = aiodns.DNSResolver(loop=loop)

async def query(name, query_type):
    try:
        return await resolver.query(name, query_type)
    except aiodns.error.DNSError as e:
        return f"查询失败: {name} - {str(e)}"

def random_to_A(main_domain):
    total = []
    sub_domains = []  # 用于存储随机生成的子域名
    # 随机循环五次
    for i in range(5):
        sub_domain = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(8, 12)))
        sub_domains.append(sub_domain)  # 添加子域名到列表
        res = query(sub_domain + "." + main_domain, 'A')
        result = loop.run_until_complete(res)
        total.append(result)
    return sub_domains, total

def random_to_cname(sub_domain):
    try:
        res = query(sub_domain, 'CNAME')
        result = loop.run_until_complete(res)
        return result
    except aiodns.error.DNSError as e:
        return f"查询失败: {sub_domain} - {str(e)}"

if __name__ == '__main__':
    parser = optparse.OptionParser("%prog " + "[options] [domain]")
    parser.add_option('-a', action="store", dest='main_domain', type='string', help='')
    parser.add_option('-c', action="store", dest='sub_domain', type='string', help='')
    (options, args) = parser.parse_args()
    main_domain = options.main_domain
    sub_domain = options.sub_domain
    if main_domain:
        sub_domains, results = random_to_A(main_domain)
        # 输出子域名和结果
        for sub_domain, result in zip(sub_domains, results):
            print(f"子域名: {sub_domain}.{main_domain}, 结果: {result}")
    elif sub_domain:
        print(str(random_to_cname(sub_domain)).replace("<", "\n<"))